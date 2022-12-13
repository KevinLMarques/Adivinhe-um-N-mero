import tkinter as tk
from PIL import ImageTk, Image
import random
#---> Importar as bibliotecas que serão usadas <---#


#---> Criar uma Janela <---
window = tk.Tk()


# Definir as dimensões da janela
window.geometry("650x500")

# Define a cor de fundo da janela
window.config(bg="#0A1F46")

#E define uma propriedade onde não é ajustavel o tamanho
window.resizable(width=False, height=False)

#Definir localização do arquivo da imagem
background_image= tk.PhotoImage(file='E:/Projeto Python/bg.png')

#Aqui definimos que a imagem será utilizada como um Label
background_label = tk.Label(window, image=background_image)

#E definimos a localização como 0 para deixar centralizado e assim, como background.
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Define o titulo da janela
window.title('Adivinhe um Número')
#E definiremos o Icone do programa:
ico = Image.open('E:/Projeto Python/icon.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)


# O código para os botões e texto, e outros
# Elementos da tela vão ser escritos aqui

TARGET = random.randint(0, 100)
RETRIES = 0

#Definimos uma def para ser o texto de informação para o jogador
def update_result(text):
    result.configure(text=text)


# criar novo jogo
def new_game():
    guess_button.config(state='normal')
    #botão fica ativo
    global TARGET, RETRIES
    TARGET = random.randint(0, 100)
    #Target será o nosso numero sorteado para o jogador adivinhar
    RETRIES = 0
    #RETRIES será o numero de tentativas

#---> Definimos duas variaveis globais com o comando "global" <---

    # e finalmente, o texto abaixo da caixa de texto informando o que fazer
    update_result(text="Advinhe um número entre\n 1 e 100")


# Continuar o jogo atual ou finalizar
def play_game():
    global RETRIES
    #chama a variavel global 'RETRIES' que será usada

    choice = int(number_form.get())
    #Definimos que a caixa de texto será escrito apenas números

    # Se o valor escrito for diferente do sorteado
    if choice != TARGET:
        RETRIES += 1
    #Será adicionado mais 1 na variavel
        result = "Chute errado! Tente novamente!"
        #E a informação abaixo da caixa de texto será essa

        #Se o valor for menor que o chute do usuario
        if TARGET < choice:
            #Vai rodar a dica
            Dica = "O Número reside entre 0 e {}".format(choice)
        else:
            #Se o valor for maior...
            Dica = "O Número reside entre {} e 100".format(choice)
        #E aqui vai mostrar a informação mais a dica
        result += "\n\nDica :\n" + Dica

    else:
        #Se acertou o numero:
        result = "Você acertou o número após {} tentativas".format(RETRIES)
        #o botão de chute será desativado
        guess_button.configure(state='disabled')
        #e a informação será trocada para isso:
        result += "\n" + "Clique em >Começar< para ir Novamente!"
    #E então vai alterar.
    update_result(result)




# Resultado e dicas do jogo
result = tk.Label(window, text="Comece a Jogar!", font=("Arial", 12, "normal", "italic"), fg="#00BFB2",
                  bg="#051126",justify=tk.LEFT)

# Botão de jogar
play_button = tk.Button(window, text="Começar", font=("Arial", 14, "bold"), fg="#3B0100", bg="#00998F",
                        command=new_game, activebackground='#00D6C8', activeforeground='#240000')

# Botão de chutar
guess_button = tk.Button(window, text="Chutar", font=("Arial", 13), state='disabled', fg="#00BFB2", bg="#0E213B",
                         command=play_game,activebackground='#00E3D4', activeforeground='#07111F')

# Botão para sair
exit_button = tk.Button(window, text="Sair", font=("Arial", 14), fg="#00BFB2", bg="#5E0302", command=exit,
                        activebackground='#240000', activeforeground='#00D6C8')

# Caixa de texto
guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 11), textvariable=guessed_number)

# Posicionar os labels


result.place(x=180, y=210)

# Posicionar os botões
exit_button.place(x=300, y=320)
guess_button.place(x=350, y=147)
play_button.place(x=170, y=320)

# Posicionar a caixa de texto
number_form.place(x=180, y=150)

# começar janela
window.mainloop()