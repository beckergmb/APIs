import os
import requests
from dotenv import load_dotenv


## STEP 1:
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def verificar_alteracao(dados):
    limite_percentual = 5
    valor_fechamento_anterior = float(dados['results'][0]['regularMarketPreviousClose'])
    valor_fechamento_atual = float(dados['results'][0]['regularMarketPrice'])
    percentual_alteracao = ((valor_fechamento_atual - valor_fechamento_anterior) / valor_fechamento_anterior) * 100
    if abs(percentual_alteracao) > limite_percentual:
        print("Novas notícias da Tesla")
    else:
        print("Os fechamentos da Tesla estão estabilizados")


#Dados do endpoint e token do BRAPI.
load_dotenv()
TOKEN = os.getenv('BRAPI_TOKEN')
ATIVO = "TSLA34"
endpoint_brapi = f'https://brapi.dev/api/quote/{ATIVO}?token={TOKEN}'

try:
    resposta = requests.get(endpoint_brapi)
    resposta.raise_for_status()
    data = resposta.json()
    verificar_alteracao(data)
except requests.exceptions.HTTPError as e:
    print(f"Erro: {e}")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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
