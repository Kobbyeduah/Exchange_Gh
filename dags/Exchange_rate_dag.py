from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from tasks.scrape_data import scrape_data, merge_with_existing_csv
from tasks.upload_to_s3 import upload_to_s3

# Define the URL of the webpage containing the table
url = 'https://www.bog.gov.gh/treasury-and-the-markets/daily-interbank-fx-rates/'

# Define AWS S3 bucket name
bucket_name = 'ghexchangerate'

# Define CSV filename
csv_filename = 'fx_rates.csv'

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 6),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'scrape_data_daily',
    default_args=default_args,
    description='Fetch data from website daily and upload to S3',
    schedule_interval='@daily',  # Run daily
)

# Define the task to scrape data
def scrape_and_upload_to_s3():
    new_data = scrape_data(url)
    if new_data is not None:
        # Merge with existing CSV
        combined_df = merge_with_existing_csv(new_data, csv_filename)
        
        # Upload to S3
        upload_to_s3(combined_df, csv_filename, bucket_name)

# Define the PythonOperator to execute the scrape_and_upload_to_s3 function
scrape_and_upload_task = PythonOperator(
    task_id='scrape_and_upload_to_s3_task',
    python_callable=scrape_and_upload_to_s3,
    dag=dag,
)

# Set task dependencies (if any)
# Example: scrape_and_upload_task.set_upstream(...)

# Define other tasks and dependencies as needed

# Set task dependencies (if any)
# Example: scrape_and_upload_task >> next_task >> ...

