import telebot
import json
import numpy
import requests
from telebot.types import Message
TOKEN = '1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80'

bot = telebot.TeleBot(TOKEN)

#if false - sum , if true - mult
mult_flag = False
user_state={}

def get_bitcoin_price():
    TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    response = requests.get(TICKER_API_URL)
    response_json = response.json()

    bitcoin_price = response_json['bpi']['USD']['rate_float']
    bitcoin_date =  response_json['time']['updated']
    return f'Bitcoin price: {bitcoin_price} USD\nDate: {bitcoin_date}'

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

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    global user_state
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}\n\nCначала выбери команду:\n   ➕сложение /sum\n   ✖️умножение /mult. \nЗатем отправляй боту числа через пробел или разделенные ; , а он будет их соответственно складывать или перемножать\n\n Команда \btc выдаст цену биткоина')
    user_state[message.from_user.id]=False
    with open('log_svblv_bot.txt','a') as f:
        print(f'User: {message.from_user.first_name} Message: {message.text}',file = f)

@bot.message_handler(commands=['sum'])
def change_flag(message: Message):
    global user_state
    user_state[message.from_user.id] =False
    bot.send_message(message.chat.id, 'Теперь отправляйте числа через пробел, или разделенные ; , бот их сложит:\nНапример:\n\n1 2 3 4 5\nили\n1;2;3;4;5')
    with open('log_svblv_bot.txt','a') as f:
        print(f'User: {message.from_user.first_name} Message: {message.text}',file = f)

@bot.message_handler(commands=['mult'])
def change_flag(message: Message):
    global user_state
    user_state[message.from_user.id] = True
    bot.send_message(message.chat.id, 'Теперь отправляйте числа через пробел, или разделенные ; , бот их перемножит:\nНапример:\n\n1 2 3 4 5\nили\n1;2;3;4;5')
    with open('log_svblv_bot.txt','a') as f:
        print(f'User: {message.from_user.first_name} Message: {message.text}',file = f)

@bot.message_handler(commands=['btc'])
def change_flag(message: Message):
   output = get_bitcoin_price()
   bot.send_message(message.chat.id , output + '\nPowered by CoinDesk\nhttps://www.coindesk.com/price/bitcoin')
   with open('log_svblv_bot.txt','a') as f:
        print(f'User: {message.from_user.first_name} Message: {message.text}, Response: {output}',file = f)


@bot.message_handler(func = lambda message: True)
def result(message: Message):
    global mult_flag
    global user_state
    if user_state.get(message.from_user.id) is not None:
        output = sum_or_mult(message.text,user_state[message.from_user.id])
    else:
        output = 'Я перезагрузил бота. Нажми еще раз\n/start'
    bot.send_message(message.chat.id , output)
    with open('log_svblv_bot.txt','a') as f:
        print(f'User: {message.from_user.first_name} Message: {message.text}, Response: {output}',file = f)

bot.polling()
