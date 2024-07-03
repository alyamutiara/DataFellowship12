import os
import json

from datetime import datetime

from airflow import DAG # type: ignore
from airflow.decorators import task # type: ignore
from airflow.operators.bash import BashOperator # type: ignore

with open("/opt/airflow/dags/playground/config.json", 'r') as f:
    dag_configs = json.load(f)

# A DAG represents a workflow, a collection of tasks
for dag_config in dag_configs:
    dag_id = dag_config["dag_id"]
    # start_date = dag_config["start_date"]
    start_date = datetime.strptime(dag_config["start_date"], '%Y-%m-%d')
    schedule = dag_config["schedule"]
    task_configs = dag_config["task_configs"]

    with DAG(dag_id, start_date=start_date, schedule=schedule, catchup=False) as dag:

        # Tasks are represented as operators
        @task()
        def extract(source_path):
            # Specify the path to the folder
            source_path = source_path

            # List all files in the folder
            files = os.listdir(source_path)

            data = []

            # Print the list of files
            for file in files:
                with open(f"{source_path}/{file}", 'r') as f:
                    data.append(json.load(f))

            return data

                # with open(target_file, 'a') as f:
                #     f.write(f"{data['id']},{data['name']}\n")

        @task()
        def transform(data, columns):
            o = ""
            for a in data:
                o += ",".join([str(a[column]) for column in columns]) + "\n"

            return o

        @task()
        def load(o, target_file):
            # target_file = config["target_file"]
            with open(target_file, 'a') as f:
                f.write(o)

        # Set dependencies between tasks
        for task_config in task_configs:
            e = extract.override(task_id=f"{task_config['name']}_extract")(task_config["source_path"])
            t = transform.override(task_id=f"{task_config['name']}_transform")(e, task_config["columns"])
            l = load.override(task_id=f"{task_config['name']}_load")(t, task_config["target_file"])

            l