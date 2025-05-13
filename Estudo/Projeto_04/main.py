import os
import requests
from dotenv import load_dotenv


def verificar_alteracao(dados, noticias):
    limite_percentual = 5
    valor_fechamento_anterior = float(dados['results'][0]['regularMarketPreviousClose'])
    valor_fechamento_atual = float(dados['results'][0]['regularMarketPrice'])
    percentual_alteracao = ((valor_fechamento_atual - valor_fechamento_anterior) / valor_fechamento_anterior) * 100
    if abs(percentual_alteracao) > limite_percentual:
        artigos = noticias['articles']
        tres_artigos = artigos[:3]
        print(tres_artigos)
    else:
        print("Os fechamentos da Tesla estão estabilizados")


def verificar_resposta_api(endpoint):
    try:
        resposta = requests.get(endpoint)
        resposta.raise_for_status()
        data = resposta.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(f"Erro ao acessar {endpoint}: {e}")
        return None


#Dados do endpoint e token do BRAPI.
load_dotenv()
BRAPI_TOKEN = os.getenv('BRAPI_TOKEN')
NEWS_TOKEN = os.getenv('NEWS_TOKEN')
ATIVO = "TSLA34"

endpoint_news = f'https://newsapi.org/v2/everything?q=Tesla&language=pt&apiKey={NEWS_TOKEN}'
resposta_news = verificar_resposta_api(endpoint_news)

endpoint_brapi = f'https://brapi.dev/api/quote/{ATIVO}?token={BRAPI_TOKEN}'
resposta_brapi = verificar_resposta_api(endpoint_brapi)
verificar_alteracao(resposta_brapi, resposta_news)

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

#Optional: Format the SMS message like this: 

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
