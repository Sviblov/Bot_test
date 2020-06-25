# 1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80

import requests
import pprint as pp

#Import the requests library

def get_bitcoin_price():
    TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    response = requests.get(TICKER_API_URL)
    response_json = response.json()

    bitcoin_price = response_json['bpi']['USD']['rate_float']
    bitcoin_date =  response_json['time']['updated']
    return f'Bitcoin price: {bitcoin_price} USD\nDate: {bitcoin_date}'

