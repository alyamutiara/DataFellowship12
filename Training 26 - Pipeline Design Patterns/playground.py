import os
import json

# Specify the path to the folder
source_path = "/Users/alya/Documents/GitHub/DataFellowship12/Training 26 - Pipeline Design Patterns/dags/playground/source"
target_file = "/Users/alya/Documents/GitHub/DataFellowship12/Training 26 - Pipeline Design Patterns/dags/playground/target/students.csv"

# List all files in the folder
files = os.listdir(source_path)

# Print the list of files
for file in files:
    with open(f"{source_path}/{file}", 'r') as f:
        data = json.load(f)
    print(data)

    with open(target_file, 'a') as f:
        f.write(f"{data['id']},{data['name']}\n")