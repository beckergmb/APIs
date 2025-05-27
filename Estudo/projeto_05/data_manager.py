class Dadoscidades:
    def __init__(self, cidade, cod_iata, menor_preco):
        self.cidade = cidade
        self.cod_iata = cod_iata
        self.menor_preco = menor_preco

    def __repr__(self):
        return f"Cidade: {self.cidade}, Código IATA: {self.cod_iata}, R$ {self.menor_preco}"


class GerenciadorDados:
    endpoint = 'https://api.sheety.co/fb2153650af24b6f0d4d35bff1436935/preçoDeViagens/prices'

    def buscar_dados_planilha(self):
        import requests
        resposta = requests.get(url=self.endpoint)
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
