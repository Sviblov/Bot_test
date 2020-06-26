# 1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80

import requests
import pprint as pp
import pandas as pd
from matplotlib import pyplot as plt
from datetime import date

API_key='91b622a97f3f689cc5ca826c1c0acbc2'

lat=35
lon=139

print(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
r=requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')

def get_weather(lat, lon):
    r=requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
    weather_info = r.json()

    output1 = f'Текущая погода в {weather_info["name"]}: {weather_info["main"]["temp"]}\n\n'
    output2 = f'Ощущается как {weather_info["main"]["feels_like"]}\n\n'
    output3 = f'Скорость ветра {weather_info["wind"]["speed"]}'

    output = output1 + output2 + output3
    return output

get_weather(lat,lon)

#Import the requests library

#data_set = pd.DataFrame({'date' : output_dict.keys() , 'Price' : output_dict.values() })
#data_set = pd.DataFrame.from_dict(output_dict, orient = "index").reset_index()
#data_set.columns = ['Date', 'Price']


#with open('Price_plot.png','w') as f:



