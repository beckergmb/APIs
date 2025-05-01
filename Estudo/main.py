import requests  # Requisições HTTP
from datetime import datetime, timedelta

MINHA_LAT = -27.641399
MINHA_LONG = -52.270401


# Verifica se a estação espacial está acima da localização informada
def iss_acima():
    resposta_iss = requests.get(url='http://api.open-notify.org/iss-now.json')  # Busca a url do api da iss para retornar a sua posição atual
    resposta_iss.raise_for_status()
    dado_iss = resposta_iss.json()  # Converte o retorno JSON para um dicionário Python
    try:
        iss_latitude = float(dado_iss['iss_position']['latitude'])
        iss_longitude = float(dado_iss['iss_position']['longitude'])
    except KeyError:
        print('Erro: A resposta da API não retornou valores esperados.')
    if MINHA_LAT - 5 <= iss_latitude <= MINHA_LAT + 5 and MINHA_LONG - 5 <= iss_longitude <= MINHA_LONG + 5:
        return True
    return False


# Verifica se atualmente é noite na posição informada (com base no nascer e por do sol)
def esta_noite():
    parametros = {
        'lat': MINHA_LAT,
        'lng': MINHA_LONG,
        'formatted': 0,
    }

    # API para obter horários de nascer e pôr do sol
    resposta = requests.get('https://api.sunrise-sunset.org/json?lat=-27.641399&lng=-52.270401&formatted=0',
                            params=parametros)
    resposta.raise_for_status()
    dado = resposta.json()

    #Conversão do horário UTC da API para datetime
    formato_api = "%Y-%m-%dT%H:%M:%S+00:00"
    nascer_sol_utc = datetime.strptime(dado['results']['sunrise'], formato_api)
    por_sol_utc = datetime.strptime(dado['results']['sunset'], formato_api)

    #Conversão para horário local.
    nascer_sol_local = nascer_sol_utc - timedelta(hours=3)
    por_sol_local = por_sol_utc - timedelta(hours=3)

    hora_nascer = nascer_sol_local.time()
    hora_por = por_sol_local.time()
    hora_atual = datetime.now().time()

    if hora_por < hora_atual < hora_nascer:
        return True
    return False

# TODO: USAR ALGUM SISTEMA PARA ENVIAR O E-MAIL COM O AVISO
if iss_acima() and esta_noite():
    pass
