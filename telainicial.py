# FORMULÁRIO PARA CADASTRO DE CLIENTES

# Bibliotecas:
from tkinter import *

# Chamando o Tkinter:
janela = Tk()

# Main:
class Aplicacao():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        janela.mainloop()
        
    def tela(self):
        self.janela.title("CADASTRO DE CLIENTES")
        self.janela.configure(background= '#708090')
        self.janela.geometry("850x550")
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 880, height= 680)
        self.janela.minsize(width=550, height=380)
        
    def frames(self):
        self.frame1 = Frame(self.janela, bd = 4, bg = '#BEBEBE', highlightbackground= 'black', highlightthickness=3 )
        self.frame1.place(relx= 0.02 , rely=0.02, relwidth= 0.96,relheight= 0.45)

        self.frame2 = Frame(self.janela, bd=4, bg='#BEBEBE', highlightbackground='black', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)
        
    def botoes(self):
        
        # Botão Pesquisar:
        self.bt_limpar = Button(self.frame1, text='LIMPAR')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Botão Procurar:
        self.bt_limpar = Button(self.frame1, text='PESQUISAR')
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Botão Novo:
        self.bt_limpar = Button(self.frame1, text='NOVO')
        self.bt_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Botão Alterar:
        self.bt_limpar = Button(self.frame1, text='ALTERAR')
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Botão Apagar:
        self.bt_limpar = Button(self.frame1, text='APAGAR')
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Entrada de Dados:
        self.lb_codigo = Label(self.frame1, text='CÓDIGO')   
        self.lb_codigo.place(relx=0.05, rely=0.05)
        

# Chamando a Função:        
Aplicacao()