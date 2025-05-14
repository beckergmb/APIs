import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

ATIVO = "TSLA34" #O ativo que deseja verificar. (lembrando que as notícias estão sendo puxadas para o ativo TSLA34.)
limite_percentual = 5 #Define qual vai ser o limite para enviar o SMS.


def encurtar_url(url_longa):
    api_url = f'http://tinyurl.com/api-create.php?url={url_longa}'
    resposta = requests.get(api_url)
    resposta.raise_for_status()  # Verifica se houve algum erro HTTP
    url_encurtada = resposta.text
    if url_encurtada.startswith('http'):
        return url_encurtada
    else:
        print(f'Resposta inesperada do TinyURL: {url_encurtada}')
        return url_longa


def enviar_mensagens(mensagem):
    TWILIO_SID = os.getenv('TWILIO_SID')
    TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
    telefone_envio = os.getenv('TELEFONE_ENVIO')
    meu_telefone = os.getenv('MEU_TELEFONE')
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        client.messages.create(
            body=mensagem,
            from_=telefone_envio,
            to=meu_telefone,
        )
    except Exception as e:
        print(f'Erro ao enviar SMS: {str(e)}')


def verificar_alteracao(dados, noticias):
    if not dados or not noticias:
        print('Erro: Dados ausentes das APIs')
        return
    valor_fechamento_anterior = float(dados['results'][0]['regularMarketPreviousClose'])
    valor_fechamento_atual = float(dados['results'][0]['regularMarketPrice'])
    percentual_alteracao = ((valor_fechamento_atual - valor_fechamento_anterior) / valor_fechamento_anterior) * 100

    if abs(percentual_alteracao) >= limite_percentual:
        artigo = noticias['articles'][0]
        simbolo = '🔺' if percentual_alteracao > 0 else '🔻'
        msg = f'TESLA {simbolo}{abs(percentual_alteracao):.1f}%\n\n'
        msg += f'➡️ {artigo['title']}\n'
        msg += f'🔗 {encurtar_url(artigo['url'])}'
        enviar_mensagens(msg)


def verificar_resposta_api(endpoint):
    try:
        resposta = requests.get(endpoint)
        resposta.raise_for_status()
        data = resposta.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(f'Erro ao acessar {endpoint}: {e}"')
        return None


#Informações principais do projeto e requisitos de apis.
load_dotenv()
BRAPI_TOKEN = os.getenv('BRAPI_TOKEN')
NEWS_TOKEN = os.getenv('NEWS_TOKEN')

#Endpoint de apis e chamada das funções.
endpoint_news = f'https://newsapi.org/v2/everything?q=Tesla&language=pt&apiKey={NEWS_TOKEN}'
resposta_news = verificar_resposta_api(endpoint_news)

endpoint_brapi = f'https://brapi.dev/api/quote/{ATIVO}?token={BRAPI_TOKEN}'
resposta_brapi = verificar_resposta_api(endpoint_brapi)
verificar_alteracao(resposta_brapi, resposta_news)
