import telebot
import json
from telebot.types import Message
TOKEN = '1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    user_name = json.dump(message.from_user)
  
    bot.reply_to(message, f'Hi, {user_name}')

@bot.message_handler(func = lambda message: True)
def input_sum(message: Message):
    bot.reply_to(message, 'test')


bot.polling()
