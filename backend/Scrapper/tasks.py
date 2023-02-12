from celery import shared_task
from .models import *
import requests
import pandas as pd

@shared_task 
def test_func():
    data = pd.read_html('https://coinmarketcap.com')
    df = pd.DataFrame(data[0])
    df = df.drop(['#','Unnamed: 11', 'Last 7 Days'], axis=1)
    df.rename(columns = {'Name':'name','Price':'price','1h %':'percent_1h', '24h %':'percent_24h',
                                '7d %':'percent_7d', 'Market Cap':'market_cap', 'Volume(24h)':'volume_24h','Circulating Supply':'circulating_supply'}, inplace = True)
    df = df.fillna('none')
    try:
        response = requests.post('http://127.0.0.1:8000/scrapApi/', json=df.to_dict('records'))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")