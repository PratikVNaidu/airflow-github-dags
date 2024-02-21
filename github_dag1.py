from airflow import DAG
from datetime import datetime
from random import randint
from airflow.operators.python_operator import PythonOperator

def random_number():
    print("random_number Task Started....")
    return randint(1,10)

dag = DAG("github_dag",start_date=datetime(2024,2,8),schedule_interval="* * * * *", catchup=False)

task_1 = PythonOperator(task_id="first_task",python_callable=random_number,dag=dag)
task_2 = PythonOperator(task_id="second_task",python_callable=random_number,dag=dag)
task_3 = PythonOperator(task_id="third_task", python_callable=random_number,dag=dag)

task_3 >> task_1 >> task_2




    
