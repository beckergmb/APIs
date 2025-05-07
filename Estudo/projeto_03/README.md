# Projeto 03 - Quiz com API, OOP e Interface Gráfica

Este projeto é uma aplicação de quiz que consome perguntas de uma API pública (Open Trivia DB) e exibe os dados em uma interface gráfica usando Tkinter. Foi desenvolvido como parte dos meus estudos em consumo de APIs, e também explora conceitos iniciais de Programação Orientada a Objetos e GUI.

> ⚠️ Algumas partes do código foram feitas antes de eu consolidar meus estudos em OOP e interfaces gráficas. A parte de API é o foco principal do aprendizado aqui.

---

## Objetivos de aprendizado

- Consumir dados de uma API pública com `requests`
- Interpretar e manipular dados JSON
- Exibir dados em uma interface gráfica com Tkinter
- Utilizar classes e objetos para organizar a lógica do quiz

---

## Resultado esperado

Um quiz de 5 perguntas com interface gráfica, exibindo cada questão da API e atualizando a pontuação conforme as 
respostas corretas/erradas.

---

## Como executar

1. **Certifique-se de que as dependências estão instaladas (use o `requirements.txt` da raiz do repositório):**
```bash
    pip install -r requirements.txt
```

2. **Execute o script principal:**
```bash
    python main.py
```

---

## Estrutura dos arquivos

- ```main.py``` — ponto de entrada do programa
- ```data.py``` — conexão e requisição à API (Open Trivia DB)
- ```question_model.py``` — modelo da pergunta como classe
- ```quiz_brain.py``` — lógica de controle do quiz
- ```ui.py``` — interface gráfica com Tkinter
- ```images/``` — ícones usados nos botões

---

## Observações

- A estrutura orientada a objetos foi implementada, mas ainda estou estudando os princípios de design, lógica e organização.
- A interface gráfica está funcional, mas foi construída com apoio de tutoriais. Ainda preciso entender melhor os 
conceitos de eventos, layouts e boas práticas com Tkinter.
- O projeto foi mantido propositalmente simples (True/False) para focar no fluxo entre API → lógica OOP → GUI.