from io import StringIO
import requests
import pandas as pd
import config

def fetch_data():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=full&symbol=TSLA&datatype=csv&apikey=' + config.api_key

    r = requests.get(url)
    if r.status_code != 200:
        return df
    
    csv_data = r.text

    df = pd.read_csv(StringIO(csv_data))

    df = df[::-1]

    df.reset_index(drop=True, inplace=True)

    return df

