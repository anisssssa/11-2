from tkinter import WORD
import requests

api_key = '0a1fe1a9-8481-4b05-b8f5-84de320d309c'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{WORD}?key={api_key}'
word = 'potato'

#root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
#final_url = f'{root_url}/{word}?key={api_key}'
res = requests.get(url)
definitions = res.json()

for definitions in definitions:
        print(definitions)