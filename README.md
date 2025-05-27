# Estudos de APIs com Python

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Este repositório documenta os meus estudos e testes com o consumo de APIs utilizando a linguagem Python.

## Objetivo
Praticar e desenvolver habilidades em:
- Consumo de APIs públicas
- Interpretação de dados JSON
- Requisições HTTP com `requests`
- Manipulação de variáveis de ambiente
- Organização de projetos e boas práticas

## Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

## Como rodar os códigos

### 1. Clone este repositório:
```bash
  git clone https://github.com/beckergmb/APIs.git
```

### 2. Instale as dependências necessárias:
```bash
  pip install -r requirements.txt
```

### 3. Acesso: 
  Vá ao diretório do projeto desejado e siga as instruções específicas no `README.md` localizado na pasta correspondente.

## Observações
- Os dados sensíveis (como tokens, e-mail e senha de app) estão protegidos via `.env` siga as instruções específicas em 
  cada pasta.

## Projetos de Estudo
- [Projeto 01 - Alerta ISS por e-mail](Estudo/projeto_01/README.md)

  Monitoramento da Estação Espacial Internacional com verificação de localização, horário e envio automático de e-mail.


- [Projeto 02 - Rastreador de hábitos](Estudo/projeto_02/README.md)
  
  Criaçao de gráfico visual de hábitos utilizando a API do Pixela.


- [Projeto 03 - Quiz com interface gráfica](Estudo/projeto_03/README.md)
  
    Quiz interativo com perguntas de uma API pública (Open Trivia DB), utilizando Tkinter e OOP para praticar 
    integração entre dados externos, lógica e interface gráfica.


- [Projeto 04 - Monitor de Variação de Ações](Estudo/projeto_04/README.md)
  
    Script completo que monitora a variação de preço da ação TSLA34 (API Brapi). Se a variação exceder 5%, busca a 
notícia mais recente (NewsAPI), encurta seu link (TinyURL) e envia um alerta formatado por SMS (Twilio) para o celular do usuário.


- [Projeto 05 - Monitor de Variação de Ações](Estudo/projeto_05/README.md)
  
  Script Python automatiza a busca por passagens aéreas mais baratas para destinos personalizados definidos em uma 
planilha do Google Sheets. Utiliza a API da Amadeus para busca de voos e envia alertas via SMS usando a Twilio.

## Créditos
Projetos realizados com base no curso:  
**"100 Days of Code – The Complete Python Pro Bootcamp"** de Angela Yu (Udemy)
