import pendulum
import json
import requests

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

default_args = {
    'owner': 'airflow',
    'start_date': pendulum.datetime(2022, 6, 1, tz="Asia/Jakarta"),
    'retries': 1,
    'retry_delay': pendulum.duration(minutes=2),
}

def selecting_input():
    hook = PostgresHook(
        postgres_conn_id="postgres_localhost",
    )
    query = "SELECT * FROM table_input"
    return hook.get_records(query)


def classify_input(ti):
    xcom_input = ti.xcom_pull(task_ids='get_input_data')
    data = [[item[1], item[2], item[3], item[4]] for item in xcom_input]
    json_input = {
        "items": data
    }
    resp = requests.post(
        url="http://host.docker.internal:8000/predict",
        headers={
            "Content-Type": "application/json"
        },
        json = json_input
    )
    json_output = resp.json()
    list_insert_query = []
    for i in range(len(data)):
        for j, item in enumerate(json_output['predictions']):
            if i == j:
                insert_data = "('{}', {}, '{}')".format(xcom_input[i][0], item, json_output['executed_at'])
                list_insert_query.append(insert_data)
    return str(list_insert_query).strip('[]')

def insert_result(ti):
    hook = PostgresHook(
        postgres_conn_id="postgres_localhost",
    )
    query = "INSERT INTO table_output (id,class,executed_at) VALUES {}".format(ti.xcom_pull(task_ids="post_predict"))
    return hook.run(query.replace('"', ''))

with DAG(
    dag_id="scheduler_predict_from_db",
    default_args=default_args,
    schedule_interval= '0 10 * * *',
) as dag:

    task1 = PythonOperator(
        task_id = 'get_input_data',
        python_callable=selecting_input
    )

    task2 = PythonOperator(
        task_id = 'post_predict',
        python_callable=classify_input
    )

    task3 = PythonOperator(
        task_id = 'insert_classify_result',
        python_callable=insert_result
    )

    task1 >> task2 >> task3

    
    