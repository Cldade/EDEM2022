from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from datetime import datetime

def saludo():
    print('Hello MDA!!')

with DAG(
    dag_id="sample_dag",
    start_date=datetime(2022, 5, 28),
    schedule_interval=None,
    tags=["sample_dag"],
    default_args={'retries': 1},
) as dag:

    # Here the corresponding tasks
    start = EmptyOperator(task_id = 'start')
    python_task = PythonOperator(task_id='python_task', python_callable=saludo)
    end = EmptyOperator(task_id = 'end')


    # Here the DAG dependencies
    start >> python_task >> end