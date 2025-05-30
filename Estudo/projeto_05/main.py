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
    mensagem = f"""
        Destino: {cidade_nome}
        Valor da passagem: R$ {voo.preco}
        Ida: {formatar_data(voo.data_ida)}
        Volta: {formatar_data(voo.data_volta)}
        """
    if voo.escala > 0:
        mensagem += f"\nEscalas: {voo.escala}"
    else:
        mensagem += "\nVoo sem escalas"
    return mensagem


def enviar_email(notificador, emails, assunto, mensagem):
    notificador.enviar_email(lista_emails=emails, assunto=assunto, corpo_mensagem=mensagem)


def calcular_periodo_busca():
    data_inicio = datetime.date.today() + datetime.timedelta(days=1)
    data_final = data_inicio + datetime.timedelta(days=PERIODO_BUSCA_MESES * 30)
    return data_inicio, data_final


def processar_voo(procurar_voos, cidade, data_inicio, data_final):
    json_voos = procurar_voos.buscar_voos(
        ORIGEM_PADRAO,
        cidade.cod_iata,
        data_inicio,
        data_final,
        voo_direto=True
    )
    voo_mais_barato = procurar_voos.encontrar_voo_mais_barato(json_voos)

    if voo_mais_barato.preco == 'N/A':
        print(f'Sem voos diretos para {cidade.cidade}. Buscando com escalas...')
        json_voos = procurar_voos.buscar_voos(
            ORIGEM_PADRAO,
            cidade.cod_iata,
            data_inicio,
            data_final,
            voo_direto=False
        )
        voo_mais_barato = procurar_voos.encontrar_voo_mais_barato(json_voos)

    return voo_mais_barato


def main():

    load_dotenv()
    telefone_envio = os.getenv('TELEFONE_ENVIO')
    meu_telefone = os.getenv('MEU_TELEFONE')

    gerenciar_dados = GerenciadorDados()
    procurar_voos = ProcurarVoos()
    notificacao = NotificationManager()
    dados_cidades = gerenciar_dados.buscar_dados_planilha()
    emails = gerenciar_dados.buscar_emails_usuarios()

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

            #Enviar sms
            notificacao.enviar_mensagem(mensagem)

            #Enviar e-mail para todos os cadastrados
            assunto = f"Voo para {cidade.cidade}"
            enviar_email(notificacao, emails, assunto, mensagem)

        else:
            print(SEPARADOR)
            print(f'Nenhum resultado encontrado para {cidade.cidade} dentro do período.')
            print(SEPARADOR)


if __name__ == "__main__":
    main()
