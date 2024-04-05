#gsutil is Google Cloud storage CLI. More info on

#Definitions
#GCP: Google Cloud Platform
#Install
#To get started with gsutil you need python (at least 2.7) and to install the Google Cloud SDK. See https://cloud.google.com/sdk/docs/ to download the right package for your environment.

#General Commands
gsutil ls #: lists all your buckets
gsutil help <topic> #: help on the topic


# Buckets
gsutil mb gs://<bucket_name> #: creates the gs://bucket_name1.

gsutil rb gs://<bucket_name> #: deletes the bucket.

# Files
gsutil cp <filename> gs://<bucket_name>/ #: copies the local filename into the bucket ****.

gsutil cp <filename> gs://<bucket_name>/directory/ #: copies the local filename into the directory ****2.

gsutil mv <src_filename> gs://<bucket_name>/directory/<tgt_filename> #: moves the local src_filename to the directory and renames it as tgt_filename

gsutil rm gs://<bucket_name>/file_or_dir #: deletes the file_or_dir object.

# Folder
gsutil cp <filename> gs://<bucket_name>/ #copies the local filename into the bucket ****.