import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData
import datetime


class ProcurarVoos:
    def __init__(self):
        load_dotenv()
        self.amadeus_api_key = os.getenv('AMADEUS_API_KEY')
        self.amadeus_secret = os.getenv('AMADEUS_SECRET')
        self.token = None

    def receber_token(self):
        url_token = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.amadeus_api_key,
            'client_secret': self.amadeus_secret
        }

        resposta = requests.post(url=url_token, headers=header, data=body)
        resposta.raise_for_status()
        dado = resposta.json()
        self.token = dado['access_token']
        return self.token

    def buscar_voos(self, origem, destino, data_inicio_busca, data_fim_busca, dias_estadia=7, voo_direto=True):
        todas_ofertas_encontradas = []
        data_busca_inicial = data_inicio_busca  # Use o objeto diretamente

        non_stop_param = 'true' if voo_direto else 'false'

        while data_busca_inicial <= data_fim_busca:  # Use o objeto diretamente
            data_de_retorno_atual = data_busca_inicial + datetime.timedelta(days=dias_estadia)

            if data_de_retorno_atual > data_fim_busca:
                data_de_retorno_atual = data_fim_busca

            data_de_partida_str = data_busca_inicial.strftime('%Y-%m-%d')
            data_de_retorno_str = data_de_retorno_atual.strftime('%Y-%m-%d')

            url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

            token_limpo = self.token.strip()
            header = {
                'Authorization': f'Bearer {token_limpo}'
            }
            params = {
                'originLocationCode': origem,
                'destinationLocationCode': destino,
                'departureDate': data_de_partida_str,
                'returnDate': data_de_retorno_str,
                'adults': 1,
                'nonStop': non_stop_param,
                'max': 50,  # Limita o número de resultados por requisição para evitar sobrecarga
                'currencyCode': 'BRL'
            }

            try:
                req = requests.Request('GET', url, headers=header, params=params).prepare()

                session = requests.Session()
                resposta = session.send(req)

                resposta.raise_for_status()
                json_resposta_atual = resposta.json()

                if 'data' in json_resposta_atual and json_resposta_atual['data']:
                    todas_ofertas_encontradas.extend(json_resposta_atual['data'])
            except requests.exceptions.RequestException as e:
                print(f'Erro ao buscar voos para {data_de_partida_str}: {e}')
            except ValueError:  # Erro ao decodificar JSON
                print(f'Erro ao decodificar resposta JSON para {data_de_partida_str}. Resposta: {resposta.text}')

            # Avance para a próxima data de partida (ex: 30 dias depois)
            data_busca_inicial += datetime.timedelta(days=30)

        return {'data': todas_ofertas_encontradas}  # Retorna no formato JSON esperado por encontrar_voo_mais_barato

    @staticmethod
    def encontrar_voo_mais_barato(dados_voo_json):
        if dados_voo_json is None or 'data' not in dados_voo_json or not dados_voo_json['data']:
            return FlightData(preco='N/A', aeroporto_origem='N/A', aeroporto_destino='N/A', data_ida='N/A', data_volta='N/A')
        voos_encontrados = dados_voo_json['data']

        try:
            voo_mais_barato_json = min(voos_encontrados, key=lambda voo: float(voo['price']['total']))
        except (KeyError, ValueError):
            print("Erro ao encontrar o voo mais barato: Preço ou estrutura de dados inesperada.")
            return FlightData(preco='N/A', aeroporto_origem='N/A', aeroporto_destino='N/A', data_ida='N/A', data_volta='N/A')

        preco = voo_mais_barato_json['price']['total']
        aeroporto_origem = voo_mais_barato_json['itineraries'][0]['segments'][0]['departure']['iataCode']
        aeroporto_destino = voo_mais_barato_json['itineraries'][0]['segments'][-1]['arrival']['iataCode']
        data_ida = voo_mais_barato_json['itineraries'][0]['segments'][0]['departure']['at'][:10]
        data_volta = voo_mais_barato_json['itineraries'][-1]['segments'][-1]['arrival']['at'][:10]
        numero_tot_segmentos = len(voo_mais_barato_json['itineraries'][0]['segments'])
        escala = numero_tot_segmentos - 1

        voo_resultante = FlightData(
            preco=preco,
            aeroporto_origem=aeroporto_origem,
            aeroporto_destino=aeroporto_destino,
            data_ida=data_ida,
            data_volta=data_volta,
            escala=escala,
        )
        return voo_resultante
