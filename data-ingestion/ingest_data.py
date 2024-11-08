# This script will handle data ingestion from source to the data lake.

import pandas as pd
from azure.storage.blob import BlobServiceClient

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string('your_connection_string')

# Function to ingest data
def ingest_data(file_path, container_name):
    # Read data using pandas
    data = pd.read_csv(file_path)
    
    # Upload data to Azure Blob Storage
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='data.csv')
    blob_client.upload_blob(data.to_csv(index=False), overwrite=True)

# Example usage
# ingest_data('local_data.csv', 'your-container-name')