import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table by its ID
        table = soup.find('table', id='table_3')

        # Check if the table is found
        if table:
            # Extract data from the table
            rows = []
            for row in table.find_all('tr'):
                cells = row.find_all('td')
                if cells:
                    data = [cell.text.strip() for cell in cells]
                    rows.append(data)

            # Convert data to DataFrame
            df = pd.DataFrame(rows)
            df.columns = ['Date', 'Currency', 'Buying_Rate', 'Selling_Rate']

            return df
        else:
            print("Table with ID 'table_3' not found.")
            return None
    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)
        return None

def merge_with_existing_csv(new_data, existing_csv_filename):
    # Read existing CSV file
    try:
        existing_df = pd.read_csv(existing_csv_filename)
    except FileNotFoundError:
        existing_df = pd.DataFrame(columns=['Date', 'Currency', 'Buying_Rate', 'Selling_Rate'])

    # Concatenate new data with existing data
    combined_df = pd.concat([new_data, existing_df], ignore_index=True)

    # Drop duplicates based on 'Date' column
    combined_df.drop_duplicates(subset='Date', inplace=True)

    # Sort DataFrame by 'Date' column in descending order
    combined_df['Date'] = pd.to_datetime(combined_df['Date'], errors='coerce')
    combined_df.sort_values(by='Date', ascending=False, inplace=True)

    return combined_df
