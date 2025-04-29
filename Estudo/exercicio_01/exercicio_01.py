#Importar uma API de mensagens aleatórias.

import requests

resposta_api = requests.get(url='https://api.kanye.rest')

dado = resposta_api.json()

try:
    mensagem = dado['quote']
    print(f'{dado}')

except KeyError:
    print(f'Erro: o API não retornou os valores esperados.')