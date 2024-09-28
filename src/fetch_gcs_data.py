import pandas as pd
from google.cloud import storage
from io import StringIO

def read_tsv_from_gcs(bucket_name, blob_path):
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_path)
        content = blob.download_as_string()

        # Directly return the TSV as a pandas DataFrame
        return pd.read_csv(StringIO(content.decode('utf-8')), sep='\t')
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    bucket_name = "eeg-data-bucket"
    blob_path = "sub-01/eeg/sub-01_electrodes.tsv"
    
    df = read_tsv_from_gcs(bucket_name, blob_path)
    
    if df is not None:
        print(df)
    else:
        print("Failed to read TSV from GCS")