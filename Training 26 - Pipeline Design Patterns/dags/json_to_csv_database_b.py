import os
import json

from datetime import datetime

from airflow import DAG # type: ignore
from airflow.decorators import task # type: ignore
from airflow.operators.bash import BashOperator # type: ignore

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="json_to_csv_database_b", start_date=datetime(2024, 5, 10), schedule="*/2 * * * *", catchup=False) as dag:

    configs = [
        {
            "name": "boygroup",
            "source_path": "/opt/airflow/dags/playground/source/database_b/boygroups",
            "columns": ["id", "name", "members", "debut"],
            "target_file": "/opt/airflow/dags/playground/target/dataset_b/boygroups.csv"
        }
    ]

    # Tasks are represented as operators
    for config in configs:
        @task(task_id=f"{config["name"]}_extract")
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

        @task(task_id=f"{config["name"]}_transform")
        def transform(data, columns):
            o = ""
            for a in data:
                o += ",".join([str(a[column]) for column in columns]) + "\n"

            return o

        @task(task_id=f"{config["name"]}_load")
        def load(o, target_file):
            # target_file = config["target_file"]
            with open(target_file, 'a') as f:
                f.write(o)

        # Set dependencies between tasks
        e = extract(config["source_path"])
        t = transform(e, config["columns"])
        load(t, config["target_file"])