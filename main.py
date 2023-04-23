from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from dados import *

#cores#
co0 = "#444466" #preto
co1 = "#feffff" #branca
co2 = "#6f9fbd" #azul
co3 = "#38576b" #valor
co4 = "#40ed3d" #letra
co5 = "#ef5350" #vermelho

#criando janela#
janela = Tk()
janela.title('Pokedex - Python - Usando Python')
janela.geometry('500x500')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

#criando frame
frame_pokemon = Frame(janela, width= 500, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def trocar_pokemon(i):
    global imagem_pokemon, pok_imagem
    pok_nome['text'] = i
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_id['text'] = pokemon[i]['tipo'][0]

    imagem_pokemon = pokemon[i]['tipo'][2]
    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_imagem = Label(frame_pokemon, relief='flat', image=imagem_pokemon, bg=co1, fg=co0)
    pok_imagem.place(x=60, y=50)

    pok_tipo.lift()

    pok_hp['text'] = pokemon[i]['status'][0]
    pok_atack['text'] = pokemon[i]['status'][1]
    pok_defesa['text'] = pokemon[i]['status'][2]
    pok_velocidade['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    pok_hb_1['text'] = pokemon[i]['habilidades'][0]
    pok_hb_2['text'] = pokemon[i]['habilidades'][1]
#nome
pok_nome = Label(frame_pokemon, text='Selecione o Pokemon!', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

#categoria
pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

#id
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)


#satus
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)
#hp
pok_hp = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)
#atack
pok_atack = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atack.place(x=15, y=375)
#defesa
pok_defesa = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=390)
#velocidade
pok_velocidade = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=405)
#total
pok_total = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=420)


#habilidades
pok_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidades.place(x=180, y=310)
#jato
pok_hb_1 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb_1.place(x=195, y=360)
#soco
pok_hb_2 = Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb_2.place(x=195, y=380)

# Menu


imagem_pokemon_01 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_01 = imagem_pokemon_01.resize((40, 40))
imagem_pokemon_01 = ImageTk.PhotoImage(imagem_pokemon_01)

pok_imagem_cabeca = Button(janela, command=lambda:trocar_pokemon('Pikatchu'), relief='raised', text='Pikatchu', width=150, overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, image=imagem_pokemon_01, bg=co1, fg=co0)
pok_imagem_cabeca.place(x=300, y=50)

imagem_pokemon_02 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon_02 = imagem_pokemon_02.resize((40, 40))
imagem_pokemon_02 = ImageTk.PhotoImage(imagem_pokemon_02)

pok_imagem_cabeca_2 = Button(janela, command=lambda:trocar_pokemon('Bulbasaur'),  relief='raised', text='Bulbasaur', width=150, overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, image=imagem_pokemon_02, bg=co1, fg=co0)
pok_imagem_cabeca_2.place(x=300, y=230)




janela.mainloop()