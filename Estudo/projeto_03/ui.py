import colorsys
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_QUESTAO = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.janela = Tk()
        self.janela.title("Quizz")
        self.janela.config(padx=20, pady=20, bg=THEME_COLOR)

        #Label de pontuação
        self.label_score = Label(fg='white', bg=THEME_COLOR, font=('Arial', 12, 'normal'))
        self.label_score.grid(row=0, column=1)

        #Canvas para exibir as perguntas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.texto_pergunta = self.canvas.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            font=FONT_QUESTAO
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Botão de verdadeiro
        imagem_certa = PhotoImage(file='images/true.png')
        self.botao_certo = Button(image=imagem_certa, highlightthickness=0, command=self.clique_certo)
        self.botao_certo.grid(row=2, column=0)

        #Botão de falso
        imagem_errada = PhotoImage(file='images/false.png')
        self.botao_errado = Button(image=imagem_errada, highlightthickness=0, command=self.clique_errado)
        self.botao_errado.grid(row=2, column=1)

        self.pegar_proxima_pergunta()

        self.janela.mainloop()

    def pegar_proxima_pergunta(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label_score.config(text=f'Pontuação: {self.quiz.score}')
            texto_questao = self.quiz.next_question()
            self.canvas.itemconfig(self.texto_pergunta, text=texto_questao)
        else:
            self.canvas.itemconfig(self.texto_pergunta, text='Você chegou ao fim do quiz.')
            self.botao_certo.config(state='disabled')
            self.botao_errado.config(state='disabled')

    def clique_certo(self):
        esta_certo = self.quiz.check_answer('True')
        self.dar_feedback(esta_certo)

    def clique_errado(self):
        esta_errado = self.quiz.check_answer('False')
        self.dar_feedback(esta_errado)

    def dar_feedback(self, esta_certo: bool):
        if esta_certo:
            self.canvas.config(bg='#acd8aa')
        else:
            self.canvas.config(bg='#a23e48')
        self.janela.after(1000, self.pegar_proxima_pergunta)
