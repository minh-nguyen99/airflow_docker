from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"DAG Created Successfully, My name is {first_name} {last_name} and I am {age} years old")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Michael')
    ti.xcom_push(key='last_name', value='Jackson')

def get_age(ti):
    ti.xcom_push(key='age', value='43')

default_args={
    'owner': 'minh',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
} 
with DAG(
    default_args=default_args,
    dag_id='dag_py_op_v7',
    description='python operator dag',
    start_date=datetime(2024, 3, 4),
    schedule='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )

    task2 = PythonOperator(
        task_id='get_name', 
        python_callable=get_name      
    )
    task3 =PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    task2>>task1
    task3>>task1
    pass
