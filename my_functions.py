import json
import numpy
import requests
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from datetime import date
import pprint as pp

def get_bitcoin_price(price_date=None):

    if price_date == None:

        TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

        response = requests.get(TICKER_API_URL)
        response_json = response.json()
  
        bitcoin_price = response_json['bpi']['USD']['rate_float']
        bitcoin_date =  response_json['time']['updated']
        return f'Bitcoin price: {bitcoin_price} USD\nDate: {bitcoin_date}\nПолучить цену на другую дату введите:\nЦена биткоина YYYY-MM-DD'
    else: 
        TICKER_API_URL = f'https://api.coindesk.com/v1/bpi/historical/close.json?start={price_date}&end={date.today()}'
        response = requests.get(TICKER_API_URL)
        response_json = response.json()
        bitcoin_price = response_json['bpi'][price_date]
        bitcoin_date = price_date
        return f'Bitcoin price: {bitcoin_price} USD\nDate: {bitcoin_date}\nПолучить цену на другую дату введите:\nЦена биткоина YYYY-MM-DD'
  
def get_bitcoin_timeseries(start_date, end_date,title):
    TICKER_API_URL = f'https://api.coindesk.com/v1/bpi/historical/close.json?start={start_date}&end={end_date}'

    response = requests.get(TICKER_API_URL)
    response_json = response.json()
    output_dict=response_json['bpi']
    data_set = pd.DataFrame.from_dict(output_dict, orient = "index").reset_index()
    data_set.columns = ['Date', 'Price']
    data_set.plot(x='Date', y='Price')
    plt.grid()
    plt.title('Special for ' + title + '\nГрафик строился от ' + str(start_date))
    plt.xticks(rotation=90)
    plt.savefig('Price_plot.png')

def get_weather(lat, lon):

    API_key='91b622a97f3f689cc5ca826c1c0acbc2'
    r=requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
    weather_info = r.json()

    output1 = f'Текущая погода в {weather_info["name"]}: {weather_info["main"]["temp"] - 273,15}\n\n'
    output2 = f'Ощущается как {weather_info["main"]["feels_like"] - 273,15}\n\n'
    output3 = f'Скорость ветра {weather_info["wind"]["speed"]} м/с'

    output = output1 + output2 + output3
    return output

def sum_or_mult(list, mult_flag):
    try:
        if ';' in list:
            numbers_list = [float(el) for el in list.split(';')]
        else:
            numbers_list = [float(el) for el in list.split()]
        if mult_flag:
            return numpy.prod(numbers_list)
        else:
            return sum(numbers_list)
    except:
        return "🤦‍♂️Это текст, а не числа через пробел, а команду нужно выбирать нажав /"
