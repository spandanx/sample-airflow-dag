from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

default_args={
    'owner':'airflowuser1',
    'start_date':days_ago(1)
}

with DAG(dag_id='test_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dags:

    ## FETCH data from upstocks
    @task()
    def sample_print_function():

        print("Called sample_print_function()")


    ## DAG Worflow- ETL Pipeline
    read_info = sample_print_function()
    