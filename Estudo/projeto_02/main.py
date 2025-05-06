import os
import sys
import requests
from dotenv import load_dotenv
from datetime import datetime

# Carrega variáveis de ambiente
load_dotenv()


# Função para validar as variáveis de ambiente
def validar_variaveis_ambiente():
    variaveis_necessarias = {
        'PIXELA_USERNAME': os.getenv('PIXELA_USERNAME'),
        'PIXELA_TOKEN': os.getenv('PIXELA_TOKEN'),
        'PIXELA_ID_GRAFICO': os.getenv('PIXELA_ID_GRAFICO')
    }

    variaveis_faltantes = []

    for nome, valor in variaveis_necessarias.items():
        if not valor:
            variaveis_faltantes.append(nome)

    if variaveis_faltantes:
        print(f'Erro: As seguintes variáveis de ambiente estão faltando ou vazias:')
        for var in variaveis_faltantes:
            print(f'- {var}')
        sys.exit(1)

    return variaveis_necessarias


# Valida e obtém as variáveis
variaveis = validar_variaveis_ambiente()
USERNAME = variaveis['PIXELA_USERNAME']
TOKEN = variaveis['PIXELA_TOKEN']
ID_GRAFICO = variaveis['PIXELA_ID_GRAFICO']

#Header para o token de acesso ao pixela.
headers = {
    'X-USER-TOKEN': TOKEN,
}

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

#Criação de usúario e token

parametro_de_usuario = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# try:
#     resposta = requests.post(url=PIXELA_ENDPOINT, json=parametro_de_usuario)
#     print(f'Resposta criação de usuário: {resposta.text}')
# except requests.exceptions.RequestException as e:
#     print(f'Erro ao criar usuário: {e}')

#Gráfico

# Para criar o gráfico
grafico_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
grafico_config = {
    'id': ID_GRAFICO,
    'name': 'Gráfico de Corridas',
    'unit': 'km',
    'type': 'float',
    'color': 'shibafu',
}

# try:
#     resposta_grafico = requests.post(url=grafico_endpoint, json=grafico_config, headers=headers)
#     print(f'Resposta criação do gráfico: {resposta_grafico.text}')
# except requests.exceptions.RequestException as e:
#     print(f'Erro ao criar gráfico: {e}')

#Manipulação dos pixels

#DATA ATUAL PARA MANIPULAÇÃO DOS PIXEIS. - PODE SER USADA UMA DAS DUAS. A DE CIMA PARA USAR A DATA DE HOJE E A DEBAIXO PARA INSERIR.
data_atual = datetime.now().strftime('%Y%m%d')
# data_atual = datetime(year=2025, month=3, day=13).strftime('%Y%m%d')

#Criação de pixel - USANDO POST NO REQUESTS
add_pixel_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID_GRAFICO}'
dados_novo_pixel = {
    'date': f'{data_atual}',
    'quantity': '',
}

# try:
#     resposta_pixel = requests.post(url=add_pixel_endpoint, json=dados_novo_pixel, headers=headers)
#     print(f'Resposta criação do pixel : {resposta_pixel.text}')
# except requests.exceptions.RequestException as e:
#     print(f'Erro ao criar pixel: {e}')

#Editar pixel - USANDO PUT NO REQUESTS
editar_pixel_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID_GRAFICO}/{data_atual}'
dados_editar_pixel = {
    'quantity': '',
}

# try:
#     resposta_pixel_edit = requests.put(url=editar_pixel_endpoint, json=dados_editar_pixel, headers=headers)
#     print(f'Resposta editar pixel: {resposta_pixel_edit.text}')
# except requests.exceptions.RequestException as e:
#     print(f'Erro ao editar pixel: {e}')

#Deletar pixel - USANDO DELETE NO REQUESTS
deletar_pixel_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID_GRAFICO}/{data_atual}'

# try:
#     resposta_pixel_delete = requests.delete(url=deletar_pixel_endpoint, headers=headers)
#     print(f'Resposta apagar pixel: {resposta_pixel_delete.text}')
# except requests.exceptions.RequestException as e:
#     print(f'Erro ao deletar pixel: {e}')
