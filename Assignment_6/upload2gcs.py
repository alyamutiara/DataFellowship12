from google.cloud import storage

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f'File {source_file_name} uploaded to {destination_blob_name}.')

# Upload users.json to GCS
upload_to_gcs('df12-assignment-bucket/Assignment 6', 'users.json', 'users.json')
