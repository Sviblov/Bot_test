# 1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80

import requests
import pprint as pp


base_url = 'https://api.telegram.org/bot1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80/'

r = requests.get(f'{base_url}getMe')

r = requests.get(f'{base_url}getUpdates')

answer = {}
answer['chat_id']=173409214
answer['text'] = 'blablabla'

r = requests.get(f'{base_url}sendMessage', data=answer)