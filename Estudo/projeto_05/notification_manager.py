import os
from dotenv import load_dotenv
from twilio.rest import Client


class NotificationManager:
    def __init__(self, numero_recebimento, numero_envio, mensagem):
        self.numero_recebimento = numero_recebimento
        self.numero_envio = numero_envio
        self.mensagem = mensagem

        load_dotenv()
        self.TWILIO_SID = os.getenv('TWILIO_SID')
        self.TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')

        if not all([self.TWILIO_SID, self.TWILIO_TOKEN]):
            raise ValueError("TWILIO_SID ou TWILIO_TOKEN não encontrados no .env")

    def enviar_mensagem(self):
        try:
            client = Client(self.TWILIO_SID, self.TWILIO_TOKEN)
            client.messages.create(
                body=self.mensagem,
                from_=self.numero_envio,
                to=self.numero_recebimento,
            )
            print("SMS enviado com sucesso!")
        except Exception as e:
            print(f'Erro ao enviar SMS: {str(e)}')
