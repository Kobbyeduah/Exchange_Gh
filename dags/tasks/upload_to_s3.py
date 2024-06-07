import pandas as pd
import boto3


def upload_to_s3(df, csv_filename, bucket_name):
    # Define AWS S3 credentials
    aws_access_key_id = 'AKIA4MTWMMWF6KHO5JMI'
    aws_secret_access_key = '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'

    # Save DataFrame to CSV
    df.to_csv(csv_filename, index=False)

    # Upload CSV file to S3
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3.upload_file(csv_filename, bucket_name, csv_filename)

    print(f"Data uploaded to S3 bucket '{bucket_name}' as '{csv_filename}'")
