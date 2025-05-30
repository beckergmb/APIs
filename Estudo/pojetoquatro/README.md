# Projeto 04 - Alerta de Variação de Ações com Notícias via SMS

Este script Python monitora a variação percentual do preço de uma ação específica (atualmente configurada para `TSLA34`)
usando a API da [Brapi](https://brapi.dev/). Se a variação de preço exceder um limite pré-definido, o script busca a 
notícia mais relevante sobre a empresa usando a [NewsAPI](https://newsapi.org/), encurta o link da notícia usando a API 
do [TinyURL](http://tinyurl.com/), e envia um alerta formatado via SMS utilizando a API da [Twilio](https://www.twilio.com/).

## Funcionalidades Implementadas

1.  **Monitoramento de Ação (Brapi):**
    * Conecta-se à API da Brapi usando um `BRAPI_TOKEN` para buscar dados de cotação da ação configurada (padrão `TSLA34`).
    * Calcula a variação percentual entre o preço atual e o fechamento do dia anterior.
2.  **Alerta e Busca de Notícias (NewsAPI):**
    * Se o valor absoluto da variação percentual exceder o `limite_percentual` (padrão 5%):
        * Conecta-se à NewsAPI usando um `NEWS_TOKEN`.
        * Busca a notícia mais recente em português sobre "Tesla".
3.  **Encurtamento de URL (TinyURL):**
    * Encurta a URL da primeira notícia obtida usando a API pública do TinyURL.
4.  **Envio de SMS (Twilio):**
    * Formata uma mensagem de alerta contendo:
        * Nome do ativo (`ATIVO`).
        * Símbolo de alta (🔺) ou baixa (🔻) com base na direção da variação.
        * Percentual da variação formatado com uma casa decimal.
        * Título da primeira notícia.
        * Link encurtado para a notícia.
    * Envia a mensagem formatada via SMS utilizando as credenciais da Twilio (`TWILIO_SID`, `TWILIO_TOKEN`) de um número de envio (`TELEFONE_ENVIO`) para um número de destino (`MEU_TELEFONE`).

## Tecnologias Utilizadas

* Python 3
* Biblioteca `requests` (para chamadas HTTP às APIs Brapi, NewsAPI, TinyURL)
* Biblioteca `python-dotenv` (para gerenciar chaves de API e credenciais)
* Biblioteca `twilio` (para integração com a API de SMS da Twilio)
* API da Brapi
* API da NewsAPI
* API do TinyURL
* API da Twilio

## Configuração Específica do Projeto

1.  **Dependências:**
    Este projeto necessita das bibliotecas `requests`, `python-dotenv`, e `twilio`. Garanta que elas estejam instaladas no seu ambiente:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Arquivo `.env`:**
    * Crie (ou edite) um arquivo chamado `.env`.
    * Adicione as seguintes linhas, substituindo pelos seus tokens e números reais:
        ```dotenv
        BRAPI_TOKEN=SEU_TOKEN_BRAPI_AQUI
        NEWS_TOKEN=SEU_TOKEN_NEWSAPI_AQUI
        TWILIO_SID=SEU_TWILIO_ACCOUNT_SID_AQUI
        TWILIO_TOKEN=SEU_TWILIO_AUTH_TOKEN_AQUI
        TELEFONE_ENVIO=SEU_NUMERO_TWILIO_AQUI_FORMATO_E164 #Ex:+1234567890
        MEU_TELEFONE=SEU_NUMERO_PESSOAL_AQUI_FORMATO_E164 #Ex:+5551999999999
        ```
    * **Onde obter as chaves:**
        * `BRAPI_TOKEN`: No site da [Brapi](https://brapi.dev/).
        * `NEWS_TOKEN`: No site da [NewsAPI](https://newsapi.org/) (procure por "API Key").
        * Credenciais Twilio (`TWILIO_SID`, `TWILIO_TOKEN`, `TELEFONE_ENVIO`): No seu painel (console) da [Twilio](https://www.twilio.com) após criar uma conta e adquirir/configurar um número de telefone com capacidade de SMS.

## Observações do Código

* O ativo monitorado (`ATIVO`) e o limite percentual (`limite_percentual`) podem ser facilmente alterados no início do script `main.py`.
* As notícias são fixas para a query "Tesla" em português. Para generalizar, seria necessário ajustar o endpoint da NewsAPI.
