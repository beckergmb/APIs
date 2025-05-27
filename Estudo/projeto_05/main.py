from dotenv import load_dotenv
from data_manager import GerenciadorDados
from flight_search import ProcurarVoos
from notification_manager import NotificationManager
import datetime
import os

ORIGEM_PADRAO = 'SAO'
PERIODO_BUSCA_MESES = 6
SEPARADOR = '-' * 70


def formatar_data(data_str):
    return datetime.datetime.strptime(data_str, "%Y-%m-%d").strftime("%d/%m/%Y")


def criar_mensagem_voo(cidade_nome, voo):
    return (
        f"Destino: {cidade_nome}\n"
        f"Valor da passagem: R$ {voo.preco}\n"
        f"Ida: {formatar_data(voo.data_ida)}\n"
        f"Volta: {formatar_data(voo.data_volta)}"
    )


def calcular_periodo_busca():
    data_inicio = datetime.date.today()
    data_final = data_inicio + datetime.timedelta(days=PERIODO_BUSCA_MESES * 30)
    return data_inicio, data_final


def processar_voo(procurar_voos, cidade, data_inicio, data_final):
    json_voos = procurar_voos.buscar_voos(
        ORIGEM_PADRAO,
        cidade.cod_iata,
        data_inicio,
        data_final
    )
    return procurar_voos.encontrar_voo_mais_barato(json_voos)


def enviar_notificacao(telefone_envio, meu_telefone, mensagem):
    notificador = NotificationManager(meu_telefone, telefone_envio, mensagem)
    notificador.enviar_mensagem()


def main():
    load_dotenv()
    telefone_envio = os.getenv('TELEFONE_ENVIO')
    meu_telefone = os.getenv('MEU_TELEFONE')

    gerenciar_dados = GerenciadorDados()
    dados_cidades = gerenciar_dados.buscar_dados_planilha()

    procurar_voos = ProcurarVoos()
    if not procurar_voos.receber_token():
        print("Erro ao obter token de acesso.")
        return

    print(SEPARADOR)
    print(f'Buscando as passagens aéreas mais baratas, com origem São Paulo...')
    print(SEPARADOR)

    data_inicio, data_final = calcular_periodo_busca()

    for cidade in dados_cidades:
        voo_mais_barato = processar_voo(procurar_voos, cidade, data_inicio, data_final)

        if voo_mais_barato and voo_mais_barato.preco != 'N/A':
            mensagem = criar_mensagem_voo(cidade.cidade, voo_mais_barato)
            enviar_notificacao(telefone_envio, meu_telefone, mensagem)
        else:
            print(f'Nenhum resultado encontrado para {cidade.cidade} dentro do período.')
            print(SEPARADOR)


if __name__ == "__main__":
    main()
