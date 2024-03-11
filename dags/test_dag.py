from airflow import DAG
from datetime  import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args={
    'owner': 'minh',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
} 

with DAG(
    dag_id='test_dag_v4',
    default_args=default_args,
    description='this is a test dag',
    start_date=datetime(2024, 3, 5, 2),
    schedule_interval='@daily'

) as dag:
    task1=BashOperator(
        task_id='first_task',
        bash_command="echo this is the first task"
    )
    task2=BashOperator(
        task_id='second_task',
        bash_command="echo this is the second task"
    ) 
    task3=BashOperator(
        task_id='third_task',
        bash_command="echo this is the third task"
    )
    #task1.set_downstream(task2)
    #task1.set_downstream(task3)
    task1>>task2 
    task1>>task3