import requests # requisições HTTP

resposta = requests.get(url='http://api.open-notify.org/iss-now.json') # Busca a url do api disponivel.
resposta.raise_for_status()

dado = resposta.json() # Converte o que for json para Python

try:
    longitude = dado['iss_position']['longitude']
    latitude = dado['iss_position']['latitude']

    print(f'A latitude da estação espacial internacional ISS é {latitude}, e a longitude {longitude}')

except KeyError:
    print('Erro: A resposta da API não retornou valores esperados.')
