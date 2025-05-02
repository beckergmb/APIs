# Estudos de APIs com Python

Este repositório serve para documentar os meus estudos e testes com consumo de APIs utilizando a linguagem Python.

Praticar com APIs públicos, interpretar respostas JSON e trabalhar com bibliotecas como o `requests`.

## Como rodar os códigos

1. Clone este repositório:
    ```bash
    git clone https://github.com/beckergmb/APIs.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure as variáveis de ambiente:
   Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```
    EMAIL_REMETENTE=seu_email
    SENHA_DO_EMAIL=sua_senha
    ```
   > ⚠️ Atenção: se for usar Gmail, essa senha não deve ser a senha normal, mas sim uma senha de aplicativo gerada nas configurações
da sua conta Google com verificação em duas etapas ativadas.
4. Execute o código principal:
    ```bash
    python Estudo/exercicio_01/main.py
    ```
   
## Dependências utilizadas

- requests
- pillow
- python-dotenv

## Status do projeto

Em andamento - Estudos e testes sendo adicionados progressivamente.

### Projetos concluídos:
- **Exercício 01 – Alerta ISS por e-mail:**  
   Monitoramento da Estação Espacial Internacional (ISS) com verificação de localização geográfica e condições noturnas, 
   envio automático de e-mail utilizando `smtplib`.  
   Algumas partes foram reorganizadas e outras funcionalidades implementadas, além do que foi apresentado originalmente 
   no curso, como o ajuste do fuso-horário para o Brasil, e a utilização da biblioteca `dotenv` para proteger informações
   sensíveis.

  

### Créditos

Este projeto foi desenvolvido com base no curso "100 Days of Code - The Complete Python Pro Bootcamp" da Angela Yu (Udemy).

