from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operator.datetime import BranchDateTimeOperator

from datetime import datetime

def isSaturday():
    if(datetime.today().weekday() == 6):
        print('Is Saturday!')
    else:
        print('Is not Saturday')

with BranchDateTimeOperator(
    dag_id="sample_dag",
    start_date=datetime(2022, 5, 28),
    schedule_interval=None,
    tags=["sample_dag"],
    default_args={'retries': 1},
) as dag:

    # Here the corresponding tasks
    start = EmptyOperator(task_id = 'start')
    python_task = PythonOperator(task_id='python_task', python_callable=isSaturday)
    end = EmptyOperator(task_id = 'end')


    # Here the DAG dependencies
    start >> python_task >> end