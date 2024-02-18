from acceldata_sdk.events.generic_event import GenericEvent
from acceldata_sdk.events.log_events import LogEvent
from acceldata_sdk.models.job import JobMetadata, Node
from acceldata_sdk.models.pipeline import CreatePipeline, PipelineMetadata
from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.job import CreateJob, JobMetadata
from acceldata_sdk.models.pipeline import PipelineRunResult, PipelineRunStatus
from datetime import datetime
import test_constants as test_const
import pprint

pp = pprint.PrettyPrinter(indent=4)
# UID of the pipeline in torch
pipeline_uid = "torch.external.integration.demo-default"
# Name of the pipeline in torch
pipeline_name = "Flow ETL External Integration Demo - Default"
# Name of the postgres datasource in torch
postgres_ds = "POSTGRES-DS"
# Name of the s3 datasource in torch
s3_ds = "S3-DS"
# Name of initial output asset which is the output of job copying generated csv data to s3 as csv
s3_customer = "s3_customers"
# Name of output asset which is the output of job joining data from 2nd csv and postgres by looking up department
# name for department id
s3_postgres_customers = "s3_customers_postgres"
# Name of postgres table where department id vs department name mapping has been created in demo schema
pg_table = "demo.dept_info"

pg_database = "customers"
# Name of postgres field to order sql query on
order_by = "customer_id"
# S3 bucket name
bucket = "airflow-sdk-demo"
# The location of initial csv file in s3 bucket
csv1 = 'demo/customers.csv'
# The location of csv file in s3 bucket after joining with data from postgres table
csv3 = 'demo/customers-with-department-info.csv'
# Number of entries to be generated
csv_size = 30

# Global variables needed across functions
parent_span_context = None
pipeline_run_id = None

torch_client = TorchClient(**test_const.torch_credentials)


# Create pipeline, pipeline run and root span in torch
def create_pipeline_and_run():
    pp.pprint("================= entering create_pipeline_and_run ==================")
    meta = PipelineMetadata(owner='sdk/pipeline-user', team='ADOC', codeLocation='...')
    pipeline_name_ = pipeline_name
    pipeline = CreatePipeline(
        uid=pipeline_uid,
        name=pipeline_name_,
        description=f'The pipeline {pipeline_name_} has been created from acceldata-sdk using External integration',
        meta=meta,
        context={'pipeline_uid': pipeline_uid, 'pipeline_name': pipeline_name_}

    )
    pipeline_res = torch_client.create_pipeline(pipeline=pipeline)
    print('Created pipeline with pipeline id :: ', pipeline_res.id)

    pipeline_run = pipeline_res.create_pipeline_run()
    global pipeline_run_id
    pipeline_run_id = pipeline_run.id
    span_name_ = f'{pipeline_uid}.root.span'
    global parent_span_context
    parent_span_context = pipeline_run.create_span(uid=span_name_)
    print("===Starting the root span for the pipeline run=====")
    parent_span_context.start()


# Create job and span in torch and return the handle of span (not bounded by span)
def create_job_span_not_bounded(job_uid, inputs, outputs, metadata, context_job, span_uid):
    print(
        "=================entering create_job_span_not_bounded for the job with uid " + job_uid + "==================")
    span_uid_temp = span_uid
    pipeline = torch_client.get_pipeline(pipeline_uid)
    pipeline_run = pipeline.get_run(pipeline_run_id)
    try:
        job = CreateJob(
            uid=job_uid,
            name=f'{job_uid} Job',
            pipeline_run_id=pipeline_run.id,
            description=f'{job_uid} created using torch job decorator',
            inputs=inputs,
            outputs=outputs,
            meta=metadata,
            context=context_job
        )
        job = pipeline.create_job(job)
        pp.pprint("Create job response: " + str(job))
    except Exception as e:
        print("Error in creating job")
        exception = e.__dict__
        print(exception)
        raise e
    else:
        pp.pprint("Successfully created job." + job_uid)
        parent_span_context1 = pipeline_run.get_root_span()

        associated_job_uids = [job_uid]
        if span_uid is None:
            span_uid_temp = job_uid
        span_context = parent_span_context1.create_child_span(
            uid=span_uid_temp,
            context_data={
                'time': str(datetime.now())
            },
            associatedJobUids=associated_job_uids)
    return span_context


# Generate data and save it a csv file
def write_file_func():
    pp.pprint("================= entering write_file_func ==================")
    context_job = {'job': 'data_gene', 'uid': 'customers.data-generation',
                   'operator': 'write_file_func'}
    span_context_parent = create_job_span_not_bounded(
        job_uid='customers.data-generation',
        inputs=[],
        outputs=[Node(job_uid='customers.s3-upload')],
        metadata=JobMetadata('Jason', 'COKE', 'https://github.com/coke/reports/customers.kt'),
        context_job=context_job,
        span_uid='customers.data.generation')
    pp.pprint("entering write_file_func")
    size = csv_size
    span_context_parent.start()
    span_context_parent.send_event(GenericEvent(
        context_data={'Size': size - 1, 'total_file': 1,
                      'schema': 'name,address,dept_id'},
        event_uid="customers.data.generation.metadata"))
    span_context_parent.send_event(LogEvent(
        context_data={'Size': size - 1, 'total_file': 1,
                      'schema': 'name,address,dept_id'},
        log_data="Customer data generated successfully."))
    # End span at the end of task
    span_context_parent.end()

    # Upload generated file to s3 bucket


def upload_file_to_s3():
    context_job = {'job': 'data_upload', 'time': str(datetime.now()), 'uid': 'customers.s3-upload',
                   'operator': 'upload_file_to_s3'}
    span_context_parent = create_job_span_not_bounded(
        job_uid='customers.s3-upload',
        inputs=[Node(job_uid='customers.data-generation')],
        outputs=[Node(asset_uid=f'{s3_ds}.{s3_customer}')],
        context_job=context_job,
        metadata=JobMetadata('Jason', 'COKE', 'https://github.com/coke/reports/customers.kt'),
        span_uid='customers.s3.upload')
    pp.pprint("entering upload_file_to_s3")
    span_context_parent.start()
    # Ends span at the end of task
    span_context_parent.end()


# Lookup dept_name from postgres table and generate updated csv file
def rds_and_s3_clubbing():
    context_job = {'job': 'data_clubbing', 'time': str(datetime.now()), 'uid': 'customers.s3-postgres-clubbing',
                   'operator': 'rds_and_s3_clubbing'}

    # Child 3
    pp.pprint(" ======== Creating Child 3 on the root span =====================")
    parent_span_context1 = create_job_span_not_bounded(
        job_uid='customers.s3-postgres-clubbing',
        inputs=[Node(asset_uid=f'{s3_ds}.{s3_customer}'), Node(asset_uid=f'{postgres_ds}.{pg_table}')],
        outputs=[Node(asset_uid=f'{s3_ds}.{s3_postgres_customers}')],
        context_job=context_job,
        metadata=JobMetadata('BEN', 'COKE', 'https://github.com/coke/reports/rds_customers.kt'),
        span_uid='customers.s3.postgres.clubbing')
    parent_span_context1.start()
    pp.pprint("entering csv_pg_s3")
    pp.pprint("reading csv file")

    # Child 3->1
    pp.pprint(" ======== Creating Child 3 -> 1 =====================")
    read_csv_span = parent_span_context1.create_child_span(
        uid="read_csv"
    )

    # 3->1 start
    pp.pprint(" ======== Starting Child 3 -> 1 =====================")
    read_csv_span.start()
    read_csv_span.send_event(
        GenericEvent(
            context_data={
                'total_file_to_be_read': 1, 'RDS_TABLES': '1',
            },
            event_uid="read_csv_data"
        )
    )
    # 3->1 end
    pp.pprint(" ======== Ending Child 3 -> 1 =====================")
    read_csv_span.end()

    # 3-> Generic event
    pp.pprint(" ======== Generic event Child 3 =====================")

    parent_span_context1.send_event(GenericEvent(
        context_data={'total_file_to_be_read': 1, 'RDS_TABLES': '1',
                      'DATA_INSERTED': 100, 'RDS_USER': 'postgres'},
        event_uid="customers.rds.migration.metadata"))

    # 3->2
    pp.pprint(" ======== Creating Child 3 -> 2 =====================")
    rds_merge_span = parent_span_context1.create_child_span(
        uid="rds_merge_data"
    )

    # 3->2 start
    pp.pprint(" ======== Starting Child 3 -> 2 =====================")
    rds_merge_span.start()

    # 3->2->1
    pp.pprint(" ======== Creating Child 3 -> 2 -> 1 =====================")
    rds_dataframe_span = rds_merge_span.create_child_span(
        uid="rds_prepare_dataframe"
    )

    # 3->2->1 start
    pp.pprint(" ======== Starting Child 3 -> 2 -> 1 =====================")
    rds_dataframe_span.start()

    # 3->2->1 end
    pp.pprint(" ======== Ending Child 3 -> 2 -> 1 =====================")
    rds_dataframe_span.end()

    # 3->2->2
    pp.pprint(" ======== Creating Child 3 -> 2 -> 2 =====================")
    rds_save_dataframe_span = rds_merge_span.create_child_span(
        uid="rds_save_dataframe",
        context_data={'client_time': str(datetime.now())}
    )

    # 3->2->2 start
    pp.pprint(" ======== Starting Child 3 -> 2 -> 2 =====================")
    rds_save_dataframe_span.start(
        context_data={'client_time': str(datetime.now())}
    )

    # 3->2->2 end
    pp.pprint(" ======== Ending Child 3 -> 2 -> 2 =====================")
    rds_save_dataframe_span.end(
        context_data={'client_time': str(datetime.now())}
    )

    # 3->2 end
    pp.pprint(" ======== Ending Child 3 -> 2 =====================")
    rds_merge_span.end(
    )

    # 3->3
    pp.pprint(" ======== Creating Child 3 -> 3 =====================")
    write_csv_span = parent_span_context1.create_child_span(
        uid="write_csv"
    )

    # 3->3 start
    pp.pprint(" ======== Starting Child 3 -> 3 =====================")
    write_csv_span.start(
    )
    print("Sending generic event for child 3->3")
    write_csv_span.send_event(
        GenericEvent(
            context_data={
                'client_time': str(datetime.now()),
                'total_file_to_be_written': 1, 'RDS_TABLES': '1'
            },
            event_uid="write_csv_data"
        )
    )
    # 3->3 end
    pp.pprint(" ======== Ending Child 3 -> 3 =====================")
    write_csv_span.end(
        context_data={'client_time': "dummy"}
    )

    # End the torch span at the end of task
    pp.pprint(" ======== Ending Child 3 =====================")
    parent_span_context1.end()


# End the torch pipeline at the end of ETL execution
def end_pipeline():
    pipeline = torch_client.get_pipeline(pipeline_uid)
    pipeline_run = pipeline.get_run(pipeline_run_id)
    parent_span = pipeline_run.get_root_span()
    parent_span.end(context_data={'dag_status': 'SUCCESS', 'time': str(datetime.now())})
    pipeline_run.update_pipeline_run(
        context_data={'status': 'success'},
        result=PipelineRunResult.SUCCESS,
        status=PipelineRunStatus.COMPLETED
    )


if __name__ == "__main__":
    # call all the functions for ETL
    pp.pprint("================= create_pipeline_and_run main ==================")
    create_pipeline_and_run()
    pp.pprint("===============Completed create_pipeline_and_run. entering write_file_func=============")
    write_file_func()
    pp.pprint("===============entering upload_file_to_s3=============")
    upload_file_to_s3()
    pp.pprint("===============entering rds_and_s3_clubbing=============")
    rds_and_s3_clubbing()
    pp.pprint("===============Completed all functions. entering end_pipeline=============")
    end_pipeline()
