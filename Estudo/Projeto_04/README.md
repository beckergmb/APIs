# Projeto 04 - Monitor de Variação de Ações

Este projeto é um script Python simples para monitorar a variação percentual do preço de uma ação específica (atualmente configurada para TSLA34) usando a API da [Brapi](https://brapi.dev/).

Este é um projeto de estudo e atualmente implementa o primeiro e segundo passo do objetivo final.

## Funcionalidades Atuais (Passo 1 e 2)

* Busca dados de cotação da ação configurada (TSLA34) na API Brapi.
* Calcula a variação percentual entre o preço de fechamento do dia anterior e o preço atual.
* Verifica se o valor absoluto dessa variação excede um limite pré-definido (atualmente 5%).
* Imprime uma mensagem simples no console indicando se a variação excedeu o limite ("Novas notícias da Tesla") ou se está estável ("Os fechamentos da Tesla estão estabilizados").
* Busca e imprime as 3 notícias mais recentes sobre "Tesla" (em português).

## Tecnologias Utilizadas

* Python 3
* Biblioteca `requests` (para fazer chamadas HTTP à API)
* Biblioteca `python-dotenv` (para gerenciar chaves de API de forma segura)
* API da Brapi (para dados de cotações)
* API da News (para dados de notícias)

## Configuração Específica do Projeto

1.  **Dependências:** Este projeto necessita das bibliotecas `requests` e `python-dotenv`. Garanta que elas estejam instaladas no seu ambiente via `pip install -r requirements.txt` na raiz do repositório.

2.  **Arquivo `.env`:**
    * crie um arquivo chamado `.env`.
    * Adicione a seguinte linha, substituindo pelo seu token real da Brapi:
        ```dotenv
        BRAPI_TOKEN=SEU_TOKEN_BRAPI_AQUI
        NEWS_TOKEN=SEU_TOKEN_NEWS_AQUI
        ```
    O resultado da verificação (se a variação excedeu 5% ou não) será impresso no console.

## Próximos Passos (Planejado)
* Implementar Passo 3: Integração com [Twilio](https://www.twilio.com/) para envio de SMS.