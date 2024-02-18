# Pipeline APIs

Acceldata Torch is a complete solution to observe the quality of the data present in your data lake and warehouse. Using Torch, you can ensure that high-quality data backs your business decisions. Torch provides you with tools to measure the quality of data in a data catalog and to never miss significant data sources. All users including analysts, data scientists, and developers, can rely on Torch to observe the data flowing in the warehouse or data lake and can rest assured that there is no loss of data. 
<br />
Acceldata SDK is used to trigger torch catalog and pipeline APIs. By creating a Torch client, all the torch apis can be accessed. 

Install `acceldata-sdk` pypi package in a python environment.
```bash
pip install acceldata-sdk
```

## Create Torch Client
Torch client is used to send data to the torch servers. It consists of various methods to communicate with the torch server. Torch client have access to catalog and pipeline APIs. To create a torch client, torch url and API keys are required. To create torch API keys, go to torch ui’s settings and generate keys for the client.

While creating a TorchClient connection to torch by default version compatibility checks between torch and sdk is enabled. If we want we can disable that check by passing `do_version_check` as `False.


```python
from acceldata_sdk.torch_client import TorchClient

torch_client = TorchClient(url='https://acceldata.host.dev:9999', access_key='******',
                         secret_key='*****************', do_version_check=True)

```

## Pipeline API 
There are various pipeline APIs are supported through Acceldata SDK. Pipeline APIs like create pipeline, add jobs and spans, initiate pipeline run et cetera. Acceldata sdk is able to send various event during span life cycle. Hence, Acceldata sdk has full control over the pipelines.

##### Create Pipeline And Job and span to bound the job
`Pipeline` represents the ETL pipeline in its entirety and will contain Asset nodes and Jobs associated. The complete pipeline definition forms the Lineage graph for all the data assets.
</br>
`Job Node` or `Process Node` represents an entity that does some job in the ETL workflow. From this representation, `Job’s input` is some assets or some other Jobs, and output is few other assets or few other Jobs.
Torch will use the set of Jobs definition in the workflow to create the Lineage, and also track version changes for the Pipeline.

Acceldata sdk provides `CreateJob` class which need to be passed to `create_job` function as a parameter to create a job.

Params for `CreateJob`:

`uid`: uid of the job. It should be unique for the job. It is a mandatory parameter.<br/>
`name`: name of the job. It is a mandatory parameter.

#### NOTE: This changed in 2.4.1 release

`pipeline_run_id`: id of the pipeline_run for which you want to add a job. It is a mandatory parameter if `job` is being created using `pipeline`. Its is not needed if job is being created using `pipeline_run`.<br/>
`description`: description of the job </br>
`inputs`: (list[Node]) input for the job. This can be uid of an asset specified using asset_uid parameter of Node object
        or it can be uid of another job specified using job_uid parameter of Node object.</br>
`outputs`: (list[Node]) output for the job.This can be uid of an asset specified using asset_uid parameter of Node object
        or it can be uid of another job specified using job_uid parameter of Node object.</br>
`meta`: Metadata of the Job</br>
`context`: context of the job</br>
`bounded_by_span`: (Boolean) This has to be set to True if the job has to be bounded with a span. Default value is false. It is an optional parameter.
`span_uid`: (String) This is uid of new span to be created. This is a mandatory parameter if bounded_by_span is set to True. <br/>
`with_explicit_time`: An optional boolean parameter used when a job is bounded by a span.
- If set to True, the child span will be started at the specified time provided in the subsequent events.
- If not set, the span will be automatically started with the current time at the moment of creation.

```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.job import CreateJob, JobMetadata, Node
from acceldata_sdk.models.pipeline import CreatePipeline, PipelineMetadata, PipelineRunResult, PipelineRunStatus

# Create pipeline
pipeline = CreatePipeline(
    uid='monthly_reporting_pipeline',
    name='Monthly reporting Pipeline',
    description='Pipeline to create monthly reporting tables',
    meta=PipelineMetadata('Vaishvik', 'acceldata_sdk_code', '...'),
    context={'key1': 'value1'}
)
torch_client = TorchClient(url="https://torch.acceldata.local", access_key="*******",
                          secret_key="******************************",do_version_check=False)
pipeline_response = torch_client.create_pipeline(pipeline=pipeline)
pipeline_run = pipeline_response.create_pipeline_run()

# Create a job using pipeline object.
# Passing of pipeline_run_id is mandatory
job = CreateJob(
    uid='monthly_sales_aggregate',
    name='Monthly Sales Aggregate',
    description='Generates the monthly sales aggregate tables for the complete year',
    inputs=[Node(asset_uid='datasource-name.database.schema.table_1')],
    outputs=[Node(job_uid='job2_uid')],
    meta=JobMetadata('vaishvik', 'backend', 'https://github.com/'),
    context={'key21': 'value21'},
    bounded_by_span=True,
    pipeline_run_id=pipeline_run.id,
    span_uid="test_shubh"
)
job_response = pipeline_response.create_job(job)

# Create a job using pipeline_run object.
# Passing of pipeline_run_id is not needed
job = CreateJob(
        uid='monthly_sales_aggregate',
        name='Monthly Sales Aggregate',
        description='Generates the monthly sales aggregate tables for the complete year',
        inputs=[Node(asset_uid='datasource-name.database.schema.table_1')],
        outputs=[Node(job_uid='job2_uid')],
        meta=JobMetadata('vaishvik', 'backend', 'https://github.com/'),
        context={'key21': 'value21'}
)
job_response_using_run = pipeline_run.create_job(job)
```
##### Create Pipeline Run And Generate Spans And Send Span Events

Pipeline run indicates the execution of the pipeline. The same pipeline can be executed multiple times and each execution (run) has new snapshot version. Each pipeline run has hierarchical span's group. A `Span` is a way to group a bunch of metrics, and they are hierarchical. It can be as granular as possible. The APIs will support creating a span object from a pipeline object, and then hierarchical spans are started from parent spans. A Span typically encompasses a process or a task and can be granular. This hierarchical system is powerful enough to model extremely complex pipeline observability flows. Optionally, a span can also be associated with a Job. This way, we can track starting and completion of Job, including the failure tracking. Start and stop are implicitly tracked for a span.

Acceldata sdk also has support for create new pipeline run, add spans in it. During the span life cycle, sdk is able to send some customs and standard span events to collect pipeline run metrics for observability.

Params for `create_span` function which is available under a `pipeline_run`

`uid`: uid of the span being created. This should be unique. This is a mandatory parameter.<br/>
`associatedJobUids`: List of job uids with which the span needs to be associated with.<br/>
`context_data`: This is dict of key-value pair providing custom context information related to a span.<br/>

Params for `create_child_span` function which is available under `span_context`. This is used to create hierarchy of span by creating a span under another span

`uid`: uid of the span being created. This should be unique. This is a mandatory parameter.<br/>
`context_data`: This is dict of key-value pair providing custom context information related to a span.<br/>
`associatedJobUids`: List of job uids with which the span needs to be associated with.
```python

from acceldata_sdk.events.generic_event import GenericEvent
from datetime import datetime

# create a pipeline run of the pipeline
pipeline_run = pipeline_response.create_pipeline_run()

# get root span of a pipeline run
root_span = pipeline_run.get_root_span()

# create span in the pipeline run
span_context = pipeline_run.create_span(uid='monthly.generate.data.span')

# check current span is root or not
span_context.is_root()

# end the span 
span_context.end()

# check if the current span has children or not
span_context.has_children()

# create a child span
child_span_context = span_context.create_child_span('monthly.generate.customer.span')

# send custom event
child_span_context.send_event(
    GenericEvent(context_data={'client_time': str(datetime.now()), 'row_count': 100}, 
                 event_uid="order.customer.join.result")
)


# abort span
child_span_context.abort()

# failed span
child_span_context.failed()

# update a pipeline run of the pipeline
updatePipelineRunRes = pipeline_run.update_pipeline_run(context_data={'key1': 'value2', 'name': 'backend'},
                                                               result=PipelineRunResult.SUCCESS,
                                                               status=PipelineRunStatus.COMPLETED)

```

##### Get Latest Pipeline Run
Acceldata sdk can get the latest pipeline run of the pipeline. With use of the latest pipeline run instance, user can continue ETL pipeline and add spans, jobs, events too. Hence, Acceldata sdk has complete access on the torch pipeline service.
Params for `get_pipeline`:

`pipeline_identity`: String parameter used to filter pipeline. It can be either id or uid of the pipeline.

```python
pipeline = torch_client.get_pipeline('monthly.reporting.pipeline')
pipeline_run = pipeline.get_latest_pipeline_run()

```
##### Get Pipeline Run with a particular pipeline run id
Acceldata sdk can get a pipeline run of the pipeline with a particular pipeline run id. With use of the pipeline run 
instance, user can continue ETL pipeline and add spans, jobs, events too. Hence, Acceldata sdk has complete access on the torch pipeline service.

Params for `get_pipeline_run`:

`pipeline_run_id`: run id of the pipeline run<br/>
`continuation_id`: continuation id of the pipeline run<br/>
`pipeline_id`: id of the pipeline to which the run belongs to<br/>
```python
pipeline_run = torch_client.get_pipeline_run(pipeline_run_id=pipeline_run_id)
pipeline = torch_client.get_pipeline(pipeline_id=pipeline_id)
pipeline_run = torch_client.get_pipeline_run(continuation_id=continuation_id, pipeline_id=pipeline.id)
pipeline_run = pipeline.get_run(continuation_id=continuation_id)
```

##### Get Pipeline details for a particular pipeline run id
Acceldata sdk can get Pipeline details for a particular pipeline run.

```python
pipeline_details = pipeline_run.get_details()
```
##### Get all spans for a particular pipeline run id
Acceldata sdk can get all spans for a particular pipeline run id.

```python
pipeline_run_spans = pipeline_run.get_spans()
```
##### Get Pipeline Runs for a pipeline
Acceldata sdk can get all pipeline runs.
Params for `get_pipeline_runs`:

`pipeline_id`: id of the pipeline
```python
runs = torch_client.get_pipeline_runs(pipeline_id)
runs = pipeline.get_runs()
```

##### Get all Pipelines
Acceldata sdk can get all pipelines.

```python
pipelines = torch_client.get_pipelines()
```

##### Delete a Pipeline
Acceldata sdk can delete a pipeline.
```python
delete_response = pipeline.delete()
```

##### Execute policy synchronously and asynchronously
Acceldata sdk provides utility function `execute_policy` to execute policies synchronously and asynchronously. This will return an object on which `get_result` and `get_status` can be called to get result and status of the execution respectively.

Params for `execute_policy`:

`sync`: Boolean parameter used to decide if the policy should be executed synchronously or asynchronously. It is a mandatory parameter. If its is set to  `True` it will return only after the execution ends. If it is set to `False` it will return immediately after starting the execution.

`policy_type`: Enum parameter used to specify the policy type. It is a mandatory parameter. It is a enum which will take values from constants as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION.

`policy_id`: String parameter used to specify the policy id to be executed. It is a mandatory parameter. 

`incremental`: Boolean parameter used to specify if the policy execution should be incremental or full. Default value is False.

`pipeline_run_id`: Long parameter used to specify Run id of the pipeline run where the policy is being executed. This can
be used to link the policy execution with a particular pipeline run.

`failure_strategy`: Enum parameter used to decide the behaviour in case of failure. Default value is DoNotFail.

* `failure_strategy` takes enum of type `FailureStrategy` which can have 3 values DoNotFail, FailOnError and FailOnWarning.

* DoNotFail will never throw. In case of failure it will log the error.
* FailOnError will Throw exception only if it's an error. In case of warning it return without any errors.
* FailOnWarning will Throw exception on warning as well as error.

To get the execution result we can call `get_policy_execution_result` on torch_client or call `get_result` on execution object which will return a result object.

Params for `get_policy_execution_result`:

`policy_type`: Enum parameter used to specify the policy type. It is a mandatory parameter. It is a enum which will take values from constants as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION.

`execution_id`: String parameter used to specify the execution id to be queried for rsult. It is a mandatory parameter. 

`failure_strategy`: Enum parameter used to decide the behaviour in case of failure. Default value is DoNotFail.

Params for `get_result`:

`failure_strategy`: Enum parameter used to decide the behaviour in case of failure. Default value is DoNotFail.

To get the current status we can call `get_policy_status` on torch_client or call `get_status` on execution object which will get the current `resultStatus` of the execution. 

params for `get_policy_status` :
`policy_type`: Enum parameter used to specify the policy type. It is a mandatory parameter. It is a enum which will take values from constants as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION.

`execution_id`: String parameter used to specify the execution id to be queried for rsult. It is a mandatory parameter. 

`get_status` does not take any parameter.

Asynchronous execution example
```python
from acceldata_sdk.torch_client import TorchClient
import acceldata_sdk.constants as const
torch_credentials = {
    'url':  'https://torch.acceldata.local:5443/torch',
    'access_key':'PJSAJALFHSHU',
    'secret_key': 'E6LLJHKGSHJJTRHGK540E5',
    'do_version_check': 'True'
}
torch_client = TorchClient(**torch_credentials)
async_executor = torch_client.execute_policy(const.PolicyType.DATA_QUALITY, 46, sync=False, failure_strategy=const.FailureStrategy.DoNotFail, pipeline_run_id=None)
# Wait for execution to get final result
execution_result = async_executor.get_result(failure_strategy=const.FailureStrategy.DoNotFail)
# Get the current status
execution_status = async_executor.get_status()
```

Synchronous execution example.
```python
from acceldata_sdk.torch_client import TorchClient
import acceldata_sdk.constants as const
torch_credentials = {
    'url':  'https://torch.acceldata.local:5443/torch',
    'access_key':'PJSAJALFHSHU',
    'secret_key': 'E6LLJHKGSHJJTRHGK540E5',
    'do_version_check': 'True'
}
torch_client = TorchClient(**torch_credentials)
# This will wait for execution to get final result
sync_executor = torch_client.execute_policy(const.PolicyType.DATA_QUALITY, 46, sync=True, failure_strategy=const.FailureStrategy.DoNotFail, pipeline_run_id=None)
# Wait for execution to get final result
execution_result = sync_executor.get_result(failure_strategy=const.FailureStrategy.DoNotFail)
# Get the current status
execution_status = sync_executor.get_status()
```

Cancel execution example.
```python
execution_result = sync_executor.cancel()
```


Example of continuing the same pipeline run across multiple ETL scripts using continuation_id

ETL1 - Here a new pipeline_run is created using a continuation_id but pipeline_run is not closed
```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.pipeline import CreatePipeline, PipelineMetadata, PipelineRunResult, PipelineRunStatus

# Create pipeline
pipeline_uid = 'monthly_reporting_pipeline'
pipeline = CreatePipeline(
    uid=pipeline_uid,
    name='Monthly reporting Pipeline',
    description='Pipeline to create monthly reporting tables',
    meta=PipelineMetadata('Vaishvik', 'acceldata_sdk_code', '...'),
    context={'key1': 'value1'}
)
torch_client = TorchClient(url="https://torch.acceldata.local", access_key="*******",
                          secret_key="******************************",do_version_check=False)
pipeline_response = torch_client.create_pipeline(pipeline=pipeline)

# A new continuation id should be generated on every run. Same continuation id cannot be reused.
cont_id = "continuationid_demo_1"
pipeline_run = pipeline_response.create_pipeline_run(continuation_id=cont_id)

# Make sure pipeline_run is not ended using the update_pipeline_run call so that same run can be used in next ETL script
```


ETL2 - This script will continue the same pipeline run from ETL1
```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.pipeline import PipelineRunResult, PipelineRunStatus

torch_client = TorchClient(url="https://torch.acceldata.local", access_key="*******",
                          secret_key="******************************",do_version_check=False)

pipeline_uid = 'monthly_reporting_pipeline'
# First get the same pipeline using the previously used UID. Then we will get the previously started pipeline_run using the continuation_id
pipeline = torch_client.get_pipeline(pipeline_uid)

# continuation_id should be a same ID used in ETL1 script so that same pipeline_run is continued in the pipeline.
cont_id = "continuationid_demo_1"
pipeline_run = pipeline.get_run(continuation_id=cont_id)
# Use this pipeline run to create span and jobs
# At the end of this script close the pipeline run using update_pipeline_run if we do not want to continue the same pipeline_run further
updatePipelineRunRes = pipeline_run.update_pipeline_run(context_data={'key1': 'value2', 'name': 'backend'},
                                                               result=PipelineRunResult.SUCCESS,
                                                               status=PipelineRunStatus.COMPLETED)

```

