import os
import smtplib
from dotenv import load_dotenv
from twilio.rest import Client
from email.message import EmailMessage


class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.TWILIO_SID = os.getenv('TWILIO_SID')
        self.TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
        self.numero_envio = os.getenv('TELEFONE_ENVIO')
        self.numero_recebimento = os.getenv('MEU_TELEFONE')
        self.email_remetente = os.getenv('EMAIL_REMETENTE')
        self.senha_app = os.getenv('SENHA_DO_EMAIL')
        self.smtp_servidor = os.getenv('SMTP_SERVIDOR')
        self.smtp_porta = int(os.getenv('SMTP_PORTA'))

        if not all([self.TWILIO_SID, self.TWILIO_TOKEN]):
            raise ValueError("TWILIO_SID ou TWILIO_TOKEN não encontrados no .env")

    def enviar_mensagem(self, mensagem):
        try:
            client = Client(self.TWILIO_SID, self.TWILIO_TOKEN)
            client.messages.create(
                body=mensagem,
                from_=self.numero_envio,
                to=self.numero_recebimento,
            )
            print("SMS enviado com sucesso!")
        except Exception as e:
            print(f'Erro ao enviar SMS: {str(e)}')

    def enviar_email(self, lista_emails, assunto, corpo_mensagem):
        with smtplib.SMTP(self.smtp_servidor, self.smtp_porta) as conexao:
            conexao.starttls()
            conexao.login(self.email_remetente, self.senha_app)
            for email in lista_emails:
                mensagem = EmailMessage()
                mensagem["Subject"] = assunto
                mensagem["From"] = self.email_remetente
                mensagem["To"] = email
                mensagem.set_content(corpo_mensagem)

                conexao.send_message(mensagem)
            print("E-mail enviado com sucesso!")
