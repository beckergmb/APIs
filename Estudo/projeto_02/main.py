import os
import requests
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
USERNAME = os.getenv('PIXELA_USERNAME')
TOKEN = os.getenv('PIXELA_TOKEN')

pixela_endpoint = 'https://pixe.la/v1/users'
#Criação de usúario e token
parametro_de_usuario = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

try:
    resposta = requests.post(url=pixela_endpoint, json=parametro_de_usuario)
    resposta.raise_for_status()
    print(f"Status: {resposta.status_code}")
    print(resposta.text)
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")

# Para criar o gráfico (numa chamada separada)
grafico_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
grafico_config = {
    'id': 'grafico1',
    'name': 'Gráfico de Corridas',
    'unit': 'km',
    'type': 'float',
    'color': 'shibafu',
}
headers = {
    'X-USER-TOKEN': TOKEN,
}

try:
    resposta_grafico = requests.post(url=grafico_endpoint, json=grafico_config, headers=headers)
    resposta_grafico.raise_for_status()
    print(f"Status do gráfico: {resposta_grafico.status_code}")
    print(resposta_grafico.text)
except requests.exceptions.RequestException as e:
    print(f"Erro ao criar gráfico: {e}")