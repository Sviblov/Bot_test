import telebot
import json
import numpy
from telebot.types import Message
TOKEN = '1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80'

bot = telebot.TeleBot(TOKEN)

#if false - sum , if true - mult
mult_flag = False
user_state={}

def sum_or_mult(list, mult_flag):
    try:
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
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}\n\nCначала выбери команду:\n   ➕сложение /sum\n   ✖️умножение /mult. \nЗатем отправляй боту числа через пробел, а он будет их соответственно складывать или перемножать')
    user_state[message.from_user.id]=False

@bot.message_handler(commands=['sum'])
def change_flag(message: Message):
    global user_state
    if user_state[message.from_user.id]:
        user_state[message.from_user.id] = not user_state[message.from_user.id]
    bot.send_message(message.chat.id, 'Теперь отправляйте через пробел числа, бот их сложит')

@bot.message_handler(commands=['mult'])
def change_flag(message: Message):
    global user_state
    if not user_state[message.from_user.id]:
        user_state[message.from_user.id] = not user_state[message.from_user.id]
    bot.send_message(message.chat.id, 'Теперь отправляйте через пробел числа, бот их перемножит')

@bot.message_handler(func = lambda message: True)
def result(message: Message):
    global mult_flag
    global user_state
    output = sum_or_mult(message.text,user_state[message.from_user.id])
    bot.send_message(message.chat.id , output)


bot.polling()
