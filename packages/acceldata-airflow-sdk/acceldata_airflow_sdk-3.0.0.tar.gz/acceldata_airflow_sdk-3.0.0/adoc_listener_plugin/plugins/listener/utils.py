from __future__ import annotations
from airflow.models.dagrun import DagRun
from airflow.models.taskinstance import TaskInstance
from airflow.models import DagBag, DagModel
from airflow.configuration import conf
from pkg_resources import parse_version

import logging
import os
import functools
import airflow
import re

from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.job import CreateJob, JobMetadata, Node
from acceldata_sdk.models.pipeline import CreatePipeline, PipelineMetadata, PipelineRunResult, PipelineRunStatus, \
    PipelineRun
from acceldata_sdk.errors import APIError, TorchSdkException
from acceldata_sdk.events.generic_event import GenericEvent

from listener.constants import PIPELINE_NAME_SUFFIX, ROOT_SPAN_SUFFIX, STARTED, PIPELINE_STATE, ENDED, \
    STATE, \
    DURATION, SUCCESS, FAILED, MESSAGE, DAG_ID, DAG_RUN_ID, TASK_RUN_ID, OPERATOR, TRY_NUMBER, MAP_INDEX, TASK_ID, \
    DURATION_UNIT, RUN_TYPE, OWNER, QUEUE, SCHEDULE_INTERVAL, DAG_URL

log = logging.getLogger(__name__)


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            log.info("Initializing singleton instance ")
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
class SingletonTorchClient:
    def __init__(self) -> None:
        self.torchClient = get_or_create_torch_client()

    def get_torch_client(self):
        return self.torchClient


def get_dag_run_url(dag_run):
    base_url=conf.get('webserver', 'BASE_URL')
    import urllib.parse
    execution_date = urllib.parse.quote(dag_run.execution_date.isoformat())
    dag_url = f'{base_url}/graph?root=&dag_id={dag_run.dag_id}&execution_date={execution_date}&arrang=LR'
    log.info(dag_url)
    return dag_url


def get_or_create_torch_client():
    #TODO: Required on Mac else the app crashes
    os.environ["no_proxy"] = "*"
    torch_catalog_url = os.environ["TORCH_CATALOG_URL"]
    access_key = os.environ["TORCH_ACCESS_KEY"]
    secret_key = os.environ["TORCH_SECRET_KEY"]
    torch_client = TorchClient(url=torch_catalog_url, access_key=access_key,
                               secret_key=secret_key)
    return torch_client


def should_ignore_dag(dag_id):
    dagids_to_ignore = os.environ.get("DAGIDS_TO_IGNORE")
    dagids_regex_to_ignore = os.environ.get("DAGIDS_REGEX_TO_IGNORE")
    ignore_dag_id = False

    # If any one of these env variables are present, ignore based on the criteria
    dag_id_match = False
    dag_id_regex_match = False
    if dagids_regex_to_ignore is not None:
        dag_id_regex_match = re.search(dagids_regex_to_ignore, dag_id)

    if dagids_to_ignore is not None:
        if dag_id in dagids_to_ignore.split(','):
            dag_id_match = True

    if dag_id_regex_match or dag_id_match:
        ignore_dag_id = True
        log.info("Ignoring dag_id %s instrumentation", dag_id)

    return ignore_dag_id


def observe_dag_env_variables_detected():
    dagids_to_observe = os.environ.get("DAGIDS_TO_OBSERVE")
    dagids_regex_to_observe = os.environ.get("DAGIDS_REGEX_TO_OBSERVE")
    log.debug("DAGIDS_TO_OBSERVE")
    log.debug(dagids_to_observe)
    log.debug("DAGIDS_REGEX_TO_OBSERVE")
    log.debug(dagids_regex_to_observe)
    if dagids_to_observe is not None or dagids_regex_to_observe is not None:
        return True
    return False


def ignore_dag_env_variables_detected():
    dagids_to_ignore = os.environ.get("DAGIDS_TO_IGNORE")
    dagids_regex_to_ignore = os.environ.get("DAGIDS_REGEX_TO_IGNORE")
    if dagids_to_ignore is not None or dagids_regex_to_ignore is not None:
        return True
    return False


def should_observe_dag(dag_id):
    dagids_to_observe = os.environ.get("DAGIDS_TO_OBSERVE")
    dagids_regex_to_observe = os.environ.get("DAGIDS_REGEX_TO_OBSERVE")

    # If any one of these env variables are present, observe based on the criteria
    observe_dag_id = False
    dag_id_match = False
    dag_id_regex_match = False

    if dagids_regex_to_observe is not None:
        dag_id_regex_match = re.search(dagids_regex_to_observe, dag_id)

    if dagids_to_observe is not None:
        if dag_id in dagids_to_observe.split(','):
            dag_id_match = True

    if dag_id_regex_match or dag_id_match:
        observe_dag_id = True
        log.info("Observing dag_id %s ", dag_id)

    return observe_dag_id


def get_torch_client() -> TorchClient:
    singleton_torch_client = SingletonTorchClient()
    return singleton_torch_client.get_torch_client()


def is_dag_run_supported_for_version(version):
    parsed_version_airflow = parse_version(version)
    parsed_version_dag_run_support = parse_version("2.5.0.dev0")
    log.debug(f"parsed_version_airflow : {parsed_version_airflow}")
    log.debug(f"parsed_version_dag_run_support : {parsed_version_dag_run_support}")
    if parsed_version_airflow >= parsed_version_dag_run_support:
        log.debug("dag_run state change events are supported ")
        return True
    log.info("dag_run state change events not supported ")
    return False


def get_downstream_ids_task_instance(task_instance: TaskInstance, session):
    dag_model = DagModel.get_current(task_instance.dag_id, session=session)
    dagbag = DagBag(dag_folder=dag_model.fileloc, read_dags_from_db=True)
    dag = dagbag.get_dag(task_instance.dag_id, session=session)
    task_ids = dag.task_dict[task_instance.task_id].downstream_task_ids
    return task_ids


def create_pipeline_for_dag_run(dag_run: DagRun, torch_client, msg: str):
    log.debug("create_pipeline_for_dag_run invoked")
    dag_id = dag_run.dag_id
    pipeline_name = dag_id
    root_span_uid = dag_id + ROOT_SPAN_SUFFIX
    dag_url = get_dag_run_url(dag_run)
    try:
        # 1. Create Pipeline
        log.info("Creating pipeline for the DAG with the pipeline_name %s", pipeline_name)
        pipeline = CreatePipeline(uid=pipeline_name, name=pipeline_name)
        pipeline_response = torch_client.create_pipeline(pipeline)
        dag_run_id = dag_run.run_id

        # 2. Create pipeline run
        log.info("Creating pipeline run for the pipeline with name %s", pipeline_name)
        log.debug(f"dag run {dag_run}")
        context_data = {
            STARTED: str(dag_run.start_date),
            STATE: str(dag_run.state),
            DAG_ID: str(dag_id),
            DAG_RUN_ID: str(dag_run_id),
            RUN_TYPE: str(dag_run.run_type),
            DAG_URL: dag_url,
            # TODO: Code breaks for the older version,
            # SCHEDULE_INTERVAL: str(dag_run.dag.schedule_interval),
            MESSAGE: msg}

        log.info("Getting the pipeline run corresponding to dag run based on continuation_id and pipeline_id")
        continuation_id = f"{dag_id}.{dag_run_id}"
        pipeline_run = pipeline_response.create_pipeline_run(context_data=context_data, continuation_id=continuation_id)
        pipeline_run_id = pipeline_run.id
        log.info("Created pipeline run with the pipeline_run_id: %s", pipeline_run_id)

        # 3. Create root span
        log.info("Creating the root span")
        root_span = pipeline_run.create_span(uid=root_span_uid)
        event_uid = f'{root_span_uid}.start_event'
        pipeline_start_event = GenericEvent(context_data=context_data,
                                            event_uid=event_uid)
        root_span.send_event(span_event=pipeline_start_event)
    except APIError as api_error:
        # 2. Pipeline doesn't exist , create pipeline with the dag id as the identity
        log.error("Pipeline creation for the pipeline : %s  failed with error:  %s", str(pipeline_name), str(api_error))


def end_pipeline_for_dag_run(dag_run: DagRun, torch_client, pipeline_run_result: PipelineRunResult,
                             pipeline_run_status: PipelineRunStatus, msg: str):
    dag_id = dag_run.dag_id
    pipeline_name = dag_id
    dag_run_id = dag_run.run_id
    log.debug("end_pipeline_for_dag_run called")
    # 1. get the pipeline corresponding to the above pipelineName
    log.debug("Getting the pipeline corresponding to the pipeline name: %s", pipeline_name)
    pipeline = torch_client.get_pipeline(pipeline_name)

    #  2. get the pipeline run for the dag run
    log.info("Getting the pipeline run corresponding to dag run based on continuation_id and pipeline_id")
    continuation_id = f"{dag_id}.{dag_run_id}"
    pipeline_run = torch_client.get_pipeline_run(continuation_id=continuation_id,
                                                 pipeline_id=pipeline.id)

    # 3. get the root span for the run and mark it as success or failure accordingly
    log.debug("Getting the root span for the pipeline run with pipeline run id: %s", pipeline_run.id)
    root_span_context = pipeline_run.get_root_span()
    log.debug("Got the root span context %s", root_span_context)

    root_span_uid = dag_run.dag_id + ROOT_SPAN_SUFFIX
    log.debug("Root span uid: %s", root_span_uid)
    event_uid = f'{root_span_uid}.end_event'
    context_data = {STARTED: str(dag_run.start_date),
                    ENDED: str(dag_run.end_date),
                    DAG_ID: str(dag_run.dag_id),
                    DAG_RUN_ID: str(dag_run.run_id),
                    RUN_TYPE: str(dag_run.run_type),
                    STATE: str(dag_run.state),
                    MESSAGE: msg}
    pipeline_end_event = GenericEvent(context_data=context_data,
                                      event_uid=event_uid)

    # 4. Mark the run as success or failure accordingly
    if pipeline_run_result == PipelineRunResult.SUCCESS:
        log.debug("pipeline_run_result is: %s", pipeline_run_result)
        root_span_context.end()
        log.info("Root span has been ended.")

    elif pipeline_run_result == PipelineRunResult.FAILURE:
        log.debug("pipeline_run_result is: %s", pipeline_run_result)
        root_span_context.failed()
        log.info("Root span has been Failed.")

    log.info("Ending the pipeline run")
    root_span_context.send_event(span_event=pipeline_end_event)
    pipeline_run.update_pipeline_run(context_data=context_data,
                                     result=pipeline_run_result,
                                     status=pipeline_run_status)


def validate_and_auto_instrument_dag(dag_id):
    # Observe the given dag if any one of below condition happens:
    observe_dag_var_detected = observe_dag_env_variables_detected()
    ignore_dag_var_detected = ignore_dag_env_variables_detected()
    # 1. None of the environment variables to observe/ignore are present
    # 2. dag_id matches the OBSERVE environment variable criteria
    # 3. dag_id doesn't match the IGNORE environment variable criteria

    if ((not observe_dag_var_detected and not ignore_dag_var_detected)
            or (observe_dag_var_detected and should_observe_dag(dag_id))
            or (ignore_dag_var_detected and not should_ignore_dag(dag_id))):
        return True
    return False


def create_job_and_span(task_instance: TaskInstance, torch_client: TorchClient):
    dag_run_id = task_instance.dag_run.run_id
    dag_id = task_instance.dag_id
    pipeline_name = str(task_instance.dag_id)
    pipeline = torch_client.get_pipeline(pipeline_name)
    log.info("Getting the pipeline run corresponding to dag run based on continuation_id and pipeline_id")
    continuation_id = f"{dag_id}.{dag_run_id}"
    pipeline_run = torch_client.get_pipeline_run(continuation_id=continuation_id,
                                                 pipeline_id=pipeline.id)
    root_span_context = pipeline_run.get_root_span()
    log.debug("Got the root span context %s", root_span_context)

    # 1. create a job with  job_uid and inputs based on upstream tasks
    upstream_list = task_instance.task.upstream_list
    input_nodes = []
    associated_job_uids = []

    # Construct node inputs
    log.debug("Constructing the input_nodes from upstream tasks")
    for upstream in upstream_list:
        job_uid = upstream.task_id
        input_nodes.append(Node(job_uid=job_uid))

    job_uid = task_instance.task_id
    associated_job_uids.append(job_uid)
    job = CreateJob(
        uid=job_uid,
        name=job_uid,
        version=pipeline_run.versionId,
        pipeline_run_id=pipeline_run.id,
        inputs=input_nodes,
        bounded_by_span=False
    )

    log.info("Creating job %s", job)
    pipeline.create_job(job)

    # 2. get the root span and then create child span on that object using the spanUid above
    # and pass the jobUid as well to this function
    log.info("Initiate Child span for job with job_uid %s", job_uid)
    child_span_uid = f'{job_uid}.span'
    log.info("associatedJobUids %s for the child span with child_span_uid %s", associated_job_uids, child_span_uid)
    child_span = root_span_context.create_child_span(uid=child_span_uid, associatedJobUids=associated_job_uids)
    log.info("Created span with child_span_uid %s", child_span_uid)

    child_span.start()
    log.info("Started the child span with child_span_uid %s", child_span_uid)
    log.info("Sending job start event the child span with child_span_uid %s", child_span_uid)

    event_uid = f'{child_span_uid}.start_event'
    context_data = {TASK_ID: str(task_instance.task_id),
                    TASK_RUN_ID: str(task_instance.run_id),
                    STARTED: str(task_instance.start_date),
                    OPERATOR: str(task_instance.operator),
                    STATE: str(task_instance.state),
                    TRY_NUMBER: str(task_instance.try_number),
                    OWNER: str(task_instance.task.owner),
                    QUEUE: str(task_instance.task.queue)}
    job_start_event = GenericEvent(context_data=context_data,
                                   event_uid=event_uid)

    child_span.send_event(span_event=job_start_event)
    log.info("Successfully sent job start event for the child span with child_span_uid %s", child_span_uid)


def end_job_and_span(task_instance: TaskInstance, torch_client: TorchClient, ):
    log.info("TaskInstance State: %s", task_instance.state)
    # 1. Get pipeline for the task
    log.info("Get pipeline for the task")
    dag_id = task_instance.dag_id
    pipeline_name = str(dag_id)
    pipeline = torch_client.get_pipeline(pipeline_name)

    #  2. get the pipeline run on the dag run
    log.info("Getting the pipeline run for the corresponding dag run based on continuation_id and pipeline_id")
    dag_run_id = task_instance.dag_run.run_id
    continuation_id = f"{dag_id}.{dag_run_id}"
    pipeline_run = torch_client.get_pipeline_run(continuation_id=continuation_id,
                                                 pipeline_id=pipeline.id)
    job_uid = task_instance.task_id

    child_span_uid = f'{job_uid}.span'
    log.info("Fetching the child span with child span uid %s", child_span_uid)
    child_span = pipeline_run.get_span(child_span_uid)

    log.info("Triggering job end events based on the task state")
    context_data = {TASK_ID: str(task_instance.task_id),
                    TASK_RUN_ID: str(task_instance.run_id),
                    STARTED: str(task_instance.start_date),
                    ENDED: str(task_instance.start_date),
                    DURATION: str(task_instance.duration) + DURATION_UNIT,
                    OPERATOR: str(task_instance.operator),
                    STATE: str(task_instance.state),
                    TRY_NUMBER: str(task_instance.try_number)}

    if str(task_instance.state) == FAILED:
        # TODO : try to extract failure reason and logs
        log.info("Task instance in failed State. Sending JobFailEvent")
        event_uid = f'{child_span_uid}.failed_event'
        job_fail_event = GenericEvent(context_data=context_data, event_uid=event_uid)
        child_span.send_event(span_event=job_fail_event)
        child_span.failed()
        log.info("Marking child span as failed")

    if str(task_instance.state) == SUCCESS:
        log.info("Task instance in success State. Sending JobEndEvent")
        event_uid = f'{child_span_uid}.success_event'
        job_end_event = GenericEvent(context_data=context_data, event_uid=event_uid)
        child_span.send_event(span_event=job_end_event)
        child_span.end()
        log.info("Marking child span as success")


def create_pipeline_for_older_versions(task_instance: TaskInstance, session):
    log.info("Checking if pipeline needs to be created for the task_instance : %s", task_instance)
    upstream_size = len(task_instance.task.upstream_list)
    log.debug("Upstream size: %s", upstream_size)
    current_version = airflow.__version__
    log.debug(f"Current Airflow Version : {current_version}")
    if upstream_size == 0:
        if not is_dag_run_supported_for_version(current_version):
            log.info("Creating the pipeline for events with zero upstream events for the Current Airflow Version: %s",
                     current_version)
            create_pipeline_for_dag_run(task_instance.dag_run, get_torch_client(), msg="", )
        else:
            log.debug("task instance initiation handling not needed to start the pipeline for the newer versions")


def end_pipeline_for_older_versions(task_instance: TaskInstance, pipelineRunResult: PipelineRunResult,
                                    pipelineRunStatus: PipelineRunStatus, session):
    log.info("Checking if pipeline needs to be ended for the task instance : %s ", task_instance)
    current_version = airflow.__version__
    log.debug(f"Current Airflow Version : {current_version}")
    task_ids = get_downstream_ids_task_instance(task_instance, session)
    log.debug("downstream task_ids: %s", task_ids)
    downstream_size = len(task_ids)
    log.debug("Downstream length: %s", downstream_size)
    if downstream_size == 0 or task_instance.state == FAILED:
        if not is_dag_run_supported_for_version(current_version):
            log.info("Either the Downstream size is 0 or task_instance is in failed state.")
            log.info("Ending the pipeline run the with the Current Airflow Version: %s",
                     current_version)
            end_pipeline_for_dag_run(task_instance.dag_run, get_torch_client(), pipelineRunResult,
                                     pipelineRunStatus, msg="")
        else:
            log.debug("task instance completion handling not needed to terminate the pipeline for the newer versions")
    else:
        log.debug("Downstream size is > 0 and task_instance state is not FAILED. Proceeding with the next tasks")
