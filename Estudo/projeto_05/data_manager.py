import os
from dotenv import load_dotenv


class Dadoscidades:
    def __init__(self, cidade, cod_iata, menor_preco):
        self.cidade = cidade
        self.cod_iata = cod_iata
        self.menor_preco = menor_preco

    def __repr__(self):
        return f"Cidade: {self.cidade}, Código IATA: {self.cod_iata}, R$ {self.menor_preco}"


class GerenciadorDados:
    def __init__(self):
        load_dotenv()
        self.endpoint_precos = os.getenv('ENDPOINT_PRECOS')
        self.endpoint_usuarios = os.getenv('ENDPOINT_USUARIOS')

    def buscar_dados_planilha(self):
        import requests
        resposta = requests.get(url=self.endpoint_precos)
        data = resposta.json()
        valores = []
        for v in data['prices']:
            dados_cidade = Dadoscidades(
                cidade=v['cidade'],
                cod_iata=v['codIata'],
                menor_preco=v['menorPreco']
            )
            valores.append(dados_cidade)
        return valores

    def buscar_emails_usuarios(self):
        import requests 
        resposta = requests.get(url=self.endpoint_usuarios)
        data = resposta.json()
        emails = []
        for u in data['users']:
            emails.append(u['eMail'])
        return emails
