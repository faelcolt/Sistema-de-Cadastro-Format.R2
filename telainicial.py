from email.mime import application
from tkinter import *

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        janela.mainloop()
    def tela(self):
        self.janela.title("CADASTRO DE CLIENTES")
        self.janela.configure(background= '#708090')
        self.janela.geometry("850x550")
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 880, height= 680)
        self.janela.minsize(width=550, height=380)
    def frames(self):
        self.frame1 = Frame(self.janela, bd = 4, bg = '#BEBEBE',
                            highlightbackground= 'black', highlightthickness=3 )
        self.frame1.place(relx= 0.02 , rely=0.02, relwidth= 0.96,relheight= 0.45)

        self.frame2 = Frame(self.janela, bd=4, bg='#BEBEBE',
                            highlightbackground='black', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)
        
Aplicacao()