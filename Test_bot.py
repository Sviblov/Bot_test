# 1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80

import requests
import pprint as pp
import pandas as pd
from matplotlib import pyplot as plt
from datetime import date

#Import the requests library

def get_bitcoin_price():
    TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    response = requests.get(TICKER_API_URL)
    response_json = response.json()

    bitcoin_price = response_json['bpi']['USD']['rate_float']
    bitcoin_date =  response_json['time']['updated']
    return f'Bitcoin price: {bitcoin_price} USD\nDate: {bitcoin_date}'

#print(get_bitcoin_price())

def get_bitcoin_timeseries(start_date, end_date, title):
    TICKER_API_URL = f'https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}'

    response = requests.get(TICKER_API_URL)
    response_json = response.json()
    output_dict=response_json['bpi']
    data_set = pd.DataFrame.from_dict(output_dict, orient = "index").reset_index()
    data_set.columns = ['Date', 'Price']
    data_set.plot(x='Date', y='Price')
    plt.grid()
    plt.title('Special for ' + title)
    plt.xticks(rotation=90)
    plt.savefig('Price_plot.png')


get_bitcoin_timeseries('2018-01-01', date.today(),' Igor2')
#data_set = pd.DataFrame({'date' : output_dict.keys() , 'Price' : output_dict.values() })
#data_set = pd.DataFrame.from_dict(output_dict, orient = "index").reset_index()
#data_set.columns = ['Date', 'Price']


#with open('Price_plot.png','w') as f:



