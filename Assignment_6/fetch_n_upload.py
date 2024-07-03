import requests
import json
from google.cloud import storage

def fetch_and_save_data(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f'Data saved to {filename}')
    else:
        print(f'Failed to fetch data. Status code: {response.status_code}')

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f'File {source_file_name} uploaded to {destination_blob_name}.')

# Fetch users data
fetch_and_save_data('https://dummyjson.com/users', 'users.json')

# Upload users.json to GCS
upload_to_gcs('df12-assignment-bucket/Assignment 6', 'users.json', 'users.json')
