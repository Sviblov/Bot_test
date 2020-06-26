import telebot
import json
import numpy
import requests
from telebot.types import Message
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from datetime import date
import pprint as pp
from telebot import types
import my_functions as mf

TOKEN = '1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80'

bot = telebot.TeleBot(TOKEN)

#if false - sum , if true - mult
mult_flag = False
user_state={}
matplotlib.use('agg')

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    global user_state
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Сложение')
    itembtn2 = types.KeyboardButton('Умножение')
    itembtn3 = types.KeyboardButton('Цена биткоина')
    itembtn4 = types.KeyboardButton('Погода',request_location=True)
    itembtn5 = types.KeyboardButton('Перезагрузить бота')
    markup.row(itembtn1, itembtn2)
    markup.row(itembtn3)
    markup.row(itembtn4)
    markup.row(itembtn5)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}\n\nCначала выбери арифметическое действие: Затем отправляй боту числа через пробел или разделенные ; , а бот будет их складывать или перемножать\n\nЕще можно узнать цену биткоина и погоду', reply_markup=markup)
    user_state[message.from_user.id]=False
    
def btc_price(message_text, user):
    output = ''
    if message_text == 'Цена биткоина' or message_text == 'цена биткоина':
        price_date =date.today()
        output = output + mf.get_bitcoin_price()
    else:
        
        price_date=message_text.split()[2]
        try:
            output = output + mf.get_bitcoin_price(price_date)
        except:
            output = 'Вы ввели что то не то \n'
            price_date = date.today()
            output = output + mf.get_bitcoin_price()
   
    
    
    return output



@bot.message_handler(content_types=['text'])
def result(message: Message):
    global mult_flag
    global user_state
    output = 'None'
    message_text = message.text
    if message_text == 'Сложение':
        user_state[message.from_user.id] = False
        bot.send_message(message.chat.id, 'Теперь отправляйте числа через пробел, или разделенные ; , бот их сложит:\nНапример:\n\n1 2 3 4 5\nили\n1;2;3;4;5')
        output = 'Теперь отправляйте числа через пробел, или разделенные ; , бот их сложит:\nНапример:\n\n1 2 3 4 5\nили\n1;2;3;4;5'

    elif message_text == 'Умножение':
        user_state[message.from_user.id] = True
        bot.send_message(message.chat.id, 'Теперь отправляйте числа через пробел, или разделенные ; , бот их перемножит:\nНапример:\n\n1 2 3 4 5\nили\n1;2;3;4;5')
        output = 'Теперь отправляйте числа через пробел, или разделенные ; , бот их перемножит:\nНапример:\n\n1 2 3 4 5\nили\n1;2;3;4;5'

    elif message_text.startswith('Цена биткоина') or message_text.startswith('цена биткоина'):
        
        output = btc_price(message_text,message.from_user.first_name)
        if output[0]=='!':
            bot.send_message(message.chat.id, output[1:])
        else:
            with open('Price_plot.png','rb') as f:
                bot.send_photo(message.chat.id,f,caption=output)
    elif message_text == 'Погода':
        pass
    elif message_text == 'Перезагрузить бота':
        send_welcome(message)
    elif message_text.split()[0]=='Привет,':
        pass
    else:
        
        if user_state.get(message.from_user.id) is not None:
            output = mf.sum_or_mult(message.text,user_state[message.from_user.id])
        else:
            output = 'Нужно перезагрузить бот в меню'
        bot.send_message(message.chat.id , output)
       
    with open('log_svblv_bot.txt','a') as f:
        old_str='\n'
        new_str=''
        print(f'User: {message.from_user.first_name} Message: {message.text}',file=f)
   



@bot.message_handler(content_types=['location'])
def handle_location(message: Message):

    output = mf.get_weather(message.location.latitude, message.location.longitude)
    
    bot.send_message(message.chat.id, output)

bot.polling()
