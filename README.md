# Daily Interbank FX Rates Data Pipeline Project

## Overview
This project aims to build a robust data pipeline for acquiring, cleaning, modeling, persisting, warehousing, and consuming daily interbank FX rates data from the [Bank of Ghana](https://www.bog.gov.gh/treasury-and-the-markets/daily-interbank-fx-rates/). The pipeline is designed to handle data extraction, transformation, and storage, providing a comprehensive dataset for further analysis and visualization.

## Project Structure
- **`scrape_data.py`**: Script for scraping daily interbank FX rates data from the Bank of Ghana website.
- **`upload_to_s3.py`**: Script for uploading the scraped data to an Amazon S3 bucket.
- **`scrape_data_dag.py`**: Airflow DAG for scheduling, monitoring, and automating the scraping and uploading tasks on a daily basis.
- **`README.md`**: Document explaining project goals, design choices, and trade-offs.
- **`requirements.txt`**: File listing the project dependencies.

## Technical Documentation (Summary)
### 1. Data Acquisition
- Utilizes `scrape_data.py` to scrape data from the Bank of Ghana website.
### 2. Data Modeling
- Cleans and transforms data within the Airflow DAG (`scrape_data_dag.py`).
### 3. Data Persistence
- Uploads the cleaned data to an S3 bucket using `upload_to_s3.py`.

## System Design
- Adopts an append system design for continuous addition of new data.
- Ensures historical record maintenance in S3.

## Technical Considerations
- Detailed technical documentation will cover specific libraries, configurations, error handling, security considerations, and trade-offs.
- Discusses the rationale behind choosing the Bank of Ghana website, web scraping, cloud-based storage, and data warehousing solutions.

## Trade-offs and Rationale
- Explores trade-offs in design decisions, benefits of using the Bank of Ghana data, advantages of cloud-based solutions, and considerations for data consumption.

## Getting Started
1. Clone the repository.
2. Install dependencies (`requirements.txt`).
3. Execute scripts in the specified order to run the data pipeline.
4. Refer to the technical documentation for detailed setup and usage instructions.

## Dependencies
- Python 3.11
- Libraries: BeautifulSoup, Pandas, Boto3, Apache Airflow, etc. (See `requirements.txt`)

## Contributors
- Peter k. Eduah


## Acknowledgments
- [Trestle Academy Ghana](https://www.trestleacademyghana.org/)
- [Bank of Ghana](https://www.bog.gov.gh/)
"""
