import boto3
import pandas as pd
import logging
from io import StringIO
from src.logger import logging

class s3_operations:
    def __init__(self, bucket_name, aws_access_key, aws_secret_key, region_name="eu-north-1"):
        """
        Initialize the s3_operations class with AWS credentials and S3 bucket details.
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=region_name,
            endpoint_url=f"https://s3.{region_name}.amazonaws.com"  
        )
        logging.info(" Connected to AWS S3 successfully")

    def fetch_file_from_s3(self, file_key):
        """
        Fetch a CSV file from the S3 bucket and return as Pandas DataFrame.
        """
        try:
            logging.info(f"Fetching file '{file_key}' from S3 bucket '{self.bucket_name}'...")
            obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_key)
            df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))
            logging.info(f" File '{file_key}' fetched successfully with {len(df)} rows.")
            return df
        except Exception as e:
            logging.exception(f" Failed to fetch '{file_key}' from S3: {e}")
            return None
