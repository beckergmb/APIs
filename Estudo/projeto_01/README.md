# Projeto 01 – Alerta ISS por e-mail 

Este projeto verifica periodicamente a localização da Estação Espacial Internacional (ISS) em relação à sua posição geográfica e envia um e-mail de alerta se ela estiver visível no céu **durante a noite**.

---

## Dependências utilizadas:

* `requests` – Para consumo de APIs HTTP (ISS e nascer/pôr do sol)
* `smtplib` – Para envio de e-mails via protocolo SMTP
* `python-dotenv` – Para ocultar e gerenciar credenciais de forma segura
* `datetime` / `time` – Para manipulação de tempo e controle de execução

---

## Aplicações além do curso:
* Conversão de horários UTC para o fuso horário do Brasil
* Uso do .env para proteger dados sensíveis
* Estrutura de projeto adequada para versionamento com Git

---

## Como executar

### 1. Instale as dependências:
```bash
   pip install -r requirements.txt
```

---

### 2. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
EMAIL_REMETENTE=seu_email
SENHA_DO_EMAIL=sua_senha
```
ATENÇÃO: Caso for usar Gmail, essa senha não deve ser sua senha normal.
Você deve gerar uma senha de aplicativo nas configurações da sua conta Google, com a verificação em duas etapas ativada. 

---

### 3. Defina a sua localização:
```
MINHA_LAT = sua_latitude
MINHA_LONG = sua_longitude
```

### 4. Execute o script:
```bash
   python Estudo/projeto_01/main.py
```

