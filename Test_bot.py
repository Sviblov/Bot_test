# 1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80

import requests
import pprint as pp


base_url = 'https://api.telegram.org/bot1237869167:AAHlSqvq9Kw5Me9g4zrCAaaVya_yCLe9s80/'

r = requests.get(f'{base_url}getUpdates')

pp.pprint(r.json())