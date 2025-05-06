# Projeto 02 – Rastreador de hábitos com Pixela

Este projeto utiliza a API do [Pixela](https://pixe.la) para criar um sistema de **rastreamento de hábitos**.  
Neste projeto, estou rastreando **distância de corridas diárias**, mas a estrutura pode ser adaptada para qualquer tipo de hábito.

---

## Status do projeto:
Em desenvolvimento, novas funcionalidades serão adicionadas.

---

## Funcionalidades
- Criação de usuário no Pixela
- Criação de gráfico personalizado
- Adição de registros
- Edição de registros existentes
- Exclusão de registros

---

## Como executar

O código está organizado em etapas sequenciais. Para usar, você precisa descomentar as seções relevantes na ordem 
correta e, no caso de manipulação de pixels, insira os dados de quantidade e a data correta.


### 1. Instale as dependências:
```bash
  pip install -r requirements.txt
```

---

### 2. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
PIXELA_USERNAME=seu_usuario_pixela
PIXELA_TOKEN=seu_token_pixela
PIXELA_ID_GRAFICO=nome_do_id_grafico_que_deseja_criar
```

---

### 3. Execute o script:
```bash
  python Estudo/projeto_02/main.py
```

### 4. Exemplo de resposta da API

Ao executar o script com sucesso, você pode receber uma resposta como esta:

```json
  Resposta criação do pixel : {"message":"Success.","isSuccess":true}
