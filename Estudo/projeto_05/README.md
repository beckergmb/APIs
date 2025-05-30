# Projeto 05 - Alerta de Passagens Aéreas com Google Sheets, SMS e E-mail
Este script Python automatiza a busca por passagens aéreas mais baratas para destinos personalizados definidos em uma 
planilha do Google Sheets. Utiliza a API da Amadeus para busca de voos e envia alertas via SMS usando a Twilio. Os dados
de destino são conectados à planilha por meio do Google Sheety.

## Funcionalidades implementadas
1. **Leitura de Dados via Sheety:**
   * Acessa uma planilha pública hospedada com Sheety.
   * Extrai os dados das cidades, códigos IATA e preços de referência.
   * Acessa uma aba de usuários para coletar os e-mails cadastrados.

2. **Busca de Voos (Amadeus API):**
   * Utiliza a API da Amadeus com autenticação via `client_id` e `client_secret.`
   * Procura passagens aéreas com origem padrão em São Paulo (SAO) para os destinos da planilha.
   * Filtra apenas voos diretos (`nonStop = true`) e simula viagens com 7 dias de estadia.

3. **Filtragem de Preço e Seleção do Voo Mais Barato:**
    * Analisa os voos disponíveis e seleciona o voo mais barato para cada destino.
    * Formata os dados da viagem (ida, volta, preço, código de aeroportos) para notificação.

4. **Envio de Notificações via SMS (Twilio)**
    * Envia uma mensagem SMS formatada para o número pessoal configurado.
    * Inclui cidade de destino, preço, data de ida e data de volta.

5. **Envio de Notificações por E-mail (SMTP):**
   * Envia e-mails para todos os usuários cadastrados na aba "users" da planilha do Sheety.
   * Cada e-mail contém as informações formatadas do voo encontrado.
   * Utiliza servidor SMTP configurado (.env) com autenticação via senha de app.

## Tecnologias utilizadas

* Python 3
* Biblioteca requests (para chamadas HTTP às APIs Amadeus e Sheety)
* Biblioteca python-dotenv (para gerenciar variáveis de ambiente)
* Biblioteca twilio (para envio de SMS)
* Biblioteca smtplib e email.message (para envio de e-mails)
* API do [Amadeus](https://developers.amadeus.com/)
* API do [Google Sheety](https://sheety.co/)
* API da [Twilio](https://www.twilio.com/)

## Configuração Específica do Projeto
1.  **Dependências:**

    Certifique-se de instalar os pacotes necessários com o comando:
    ```bash
    pip install -r requirements.txt
    ```
2. **Arquivo `.env`** 

    Crie (ou edite) o arquivo chamado .env com as seguintes variáveis:
    ```
   AMADEUS_API_KEY=SEU_CLIENT_ID_DA_AMADEUS
   AMADEUS_SECRET=SEU_CLIENT_SECRET_DA_AMADEUS
   TWILIO_SID=SEU_TWILIO_ACCOUNT_SID
   TWILIO_TOKEN=SEU_TWILIO_AUTH_TOKEN
   TELEFONE_ENVIO=SEU_NUMERO_TWILIO_E164     # Ex: +14155552671
   MEU_TELEFONE=SEU_NUMERO_PESSOAL_E164      # Ex: +5511999999999
   ENDPOINT_PRECOS=URL_DA_ABA_DE_PRECOS      
   ENDPOINT_USUARIOS=URL_DA_ABA_DE_USUARIOS  
   EMAIL_REMETENTE=SEU_EMAIL_REMETENTE       # Ex: seuemail@gmail.com
   SENHA_DO_EMAIL=SENHA_DO_APP               # Senha de app do Gmail ou similar
   SMTP_SERVIDOR=smtp.gmail.com              # Ou outro servidor, conforme o e-mail
   SMTP_PORTA=587
    ```
   Como obter: 
    * `AMADEUS_API_KEY` e `AMADEUS_SECRET`: Crie uma conta gratuita na Amadeus for Developers.
    * `TWILIO_TOKEN` é fornecido dentro no código.
    * `TWILIO_SID`, `TWILIO_TOKEN`, `TELEFONE_ENVIO`: No seu painel da Twilio.

## Observações do Código

* O ponto de entrada é o arquivo `main.py`, que orquestra o fluxo completo.
* A planilha usada (Google) deve conter colunas `cidade`, `codIata`, e `menorPreco`.
* A busca ocorre em janelas mensais por um total de 6 meses, com duração fixa de 7 dias por viagem.
* O código é modularizado com uso de Programação Orientada a Objetos (OOP).
