from tkinter import *
import requests
from PIL import Image, ImageTk

window = Tk()
window.title("Kanye Diz...")
window.config(padx=0, pady=0)

# IMAGEM DE FUNDO
imagem_fundo = Image.open("background.png")
largura, altura = imagem_fundo.size
imagem_fundo = imagem_fundo.resize((largura, altura))
background_img = ImageTk.PhotoImage(imagem_fundo)  # <- agora funciona, pois o Tk já foi criado

# CANVAS
canvas = Canvas(width=largura, height=altura, highlightthickness=0)
canvas.create_image(0, 0, image=background_img, anchor=NW)
canvas.grid(row=0, column=0)


# CITAÇÃO
def obter_citacao():
    resposta_api = requests.get(url='https://api.kanye.rest')
    try:
        dado = resposta_api.json()
        return dado['quote']
    except KeyError:
        return "Erro ao buscar citação."


def atualizar_texto():
    nova_citacao = obter_citacao()
    canvas.itemconfig(texto_sitacao, text=nova_citacao)


texto_sitacao = canvas.create_text(
    largura // 2,
    altura // 2,
    text=obter_citacao(),
    width=300,
    font=("Georgia", 22),
    fill="gray15"
)

# BOTÃO
imagem_botao = Image.open("kanye.png")
imagem_botao = imagem_botao.resize((60, 60))
kanye_img = ImageTk.PhotoImage(imagem_botao)

kanye_botao = Button(
    image=kanye_img,
    command=atualizar_texto,
    highlightthickness=0,
    bd=0
)
canvas.create_window(largura // 2, altura - 40, window=kanye_botao)

# LOOP PRINCIPAL
window.mainloop()
