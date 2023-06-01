import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Cores
co0 = "#FFFFFF"  # branco
co1 = "#333333"  # preto
co2 = "#fcc058"  # laranja
co3 = "#fff873"  # amarelo
co4 = "#34eb3d"  # verde
co5 = "#e85151"  # vermelho
fundo = "#3b3b3b"

# Configurando a janela
janela = Tk()
janela.title('Jogo')
janela.geometry('260x280')
janela.configure(bg=fundo)

# Dividindo a janela
frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Configurando o frame de cima
app_1 = Label(frame_cima, text='Você', height=1, anchor='center', font='Ivy 10 bold', bg=co1, fg=co0)
app_1.place(x=30, y=70)
app_1_linha = Label(frame_cima, text='', height=10, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text='0', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
app_1_pontos.place(x=55, y=20)

app_ = Label(frame_cima, text=':', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
app_.place(x=125, y=20)

app_2 = Label(frame_cima, text='PC', height=1, anchor='center', font='Ivy 10 bold', bg=co1, fg=co0)
app_2.place(x=200, y=70)
app_2_linha = Label(frame_cima, text='', height=10, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)
app_2_pontos = Label(frame_cima, text='0', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
app_2_pontos.place(x=175, y=20)

app_linha = Label(frame_cima, text='', width=255, anchor='center', font='Ivy 1 bold', bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_pc = Label(frame_baixo, text='', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
app_pc.place(x=190, y=10)

# Variaveis Globais

global voce
global pc
global rounds
global pontos_voce
global pontos_pc
global icon_1
global icon_2
global icon_3
global b_icon_1
global b_icon_2
global b_icon_3

pontos_voce = 0
pontos_pc = 0
rounds = 5


# Função da lógica do jogo

def jogar(i):
    global rounds
    global pontos_voce
    global pontos_pc

    if rounds > 0:
        print(rounds)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = i
        app_pc['text'] = pc
        app_pc['fg'] = co1

        # caso for igual
        if voce == 'Pedra' and pc == 'Pedra':
            print('Empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif voce == 'Papel' and pc == 'Papel':
            print('Empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        elif voce == 'Tesoura' and pc == 'Tesoura':
            print('Empate')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
        elif voce == 'Pedra' and pc == 'Papel':
            print('Pc ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10
        elif voce == 'Pedra' and pc == 'Papel':
            print('Você ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_voce += 10
        elif voce == 'Papel' and pc == 'Tesoura':
            print('Pc ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10
        elif voce == 'Tesoura' and pc == 'Papel':
            print('Você ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_voce += 10
        elif voce == 'Tesoura' and pc == 'Pedra':
            print('Pc ganhou')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co4
            app_linha['bg'] = co0
            pontos_pc += 10
        elif voce == 'Papel' and pc == 'Pedra':
            print('Você ganhou')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_voce += 10
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc
        rounds -= 1
    else:
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc
        fim_do_jogo()


# Função do início do jogo

def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3
    global voce
    global pc
    global rounds
    global pontos_voce
    global pontos_pc
    b_jogar.destroy()

    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50, 50), Image.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=co0,
                      fg=co0, font='Ivy 10 bold',
                      anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50, 50), Image.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=co0,
                      fg=co0, font='Ivy 10 bold',
                      anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y=60)

    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50, 50), Image.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, width=50, command=lambda: jogar('Tesoura'), image=icon_3, compound=CENTER, bg=co0,
                      fg=co0, font='Ivy 10 bold',
                      anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y=60)


# Função do fim do jogo


def fim_do_jogo():
    global rounds
    global pontos_voce
    global pontos_pc

    pontos_voce = 0
    pontos_pc = 0
    rounds = 5

    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    jogador_voce = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])

    if jogador_voce > jogador_pc:
        app_vencedor = Label(frame_baixo, text='Você conseguiu! Bela Vitória', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co4)
        app_vencedor.place(x=5, y=60)
    elif jogador_pc > jogador_voce:
        app_vencedor = Label(frame_baixo, text='Que pena, não foi dessa vez!', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co5)
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text='Que disputa! Dessa vez foi empate...', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co1)
        app_vencedor.place(x=5, y=60)

    def jogar_denovo():
        app_1_pontos['text'] = 0
        app_2_pontos['text'] = 0

        app_vencedor.destroy()

        b_jogar_denovo.destroy()

        iniciar_jogo()

    b_jogar_denovo = Button(frame_baixo, command=jogar_denovo, width=30, text='Jogar de novo', bg=fundo, fg=co0, font='Ivy 10 bold', anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=5, y=151)


b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=co0, font='Ivy 10 bold',
                 anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)

janela.mainloop()