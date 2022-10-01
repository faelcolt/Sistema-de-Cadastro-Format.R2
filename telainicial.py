# Bibliotecas:
from tkinter import *

# Chamando o Tkinter:
janela = Tk()

# Main:
class App():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        janela.mainloop()
  
    def tela(self):
        self.janela.title("SYS - CAD - FR2")
        self.janela.configure(background= '#1e3743')
        self.janela.geometry("850x550")
        self.janela.resizable(True, True)
        self.janela.maxsize(width= 900, height= 700)
        self.janela.minsize(width=500, height=400)
        
    def frames(self):
        self.frame1 = Frame(self.janela, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame1.place(relx= 0.02 , rely=0.02, relwidth= 0.96, relheight= 0.46)

        self.frame2 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        
    def botoes(self):
        
        # Botão Limpar:
        self.bt_limpar = Button(self.frame1, text='LIMPAR', bd=4, bg='#8B8B83', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Botão Procurar:
        self.bt_limpar = Button(self.frame1, text='PESQUISAR', bd=4, bg='#8B8B83', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Botão Novo:
        self.bt_limpar = Button(self.frame1, text='NOVO', bd=4, bg='#8B8B83', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Botão Alterar:
        self.bt_limpar = Button(self.frame1, text='ALTERAR', bd=4, bg='#8B8B83', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        
        # Botão Apagar:
        self.bt_limpar = Button(self.frame1, text='APAGAR', bd=4, bg='#8B8B83', fg='white', font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        
        
        #======================================================================================================================================================#
        
        
        # Entrada de Dados:
        self.lb_codigo = Label(self.frame1, text='CÓDIGO', bg='#dfe3ee', fg='#107db2')   
        self.lb_codigo.place(relx=0.05, rely=0.05)
        self.codigo_entry = Entry(self.frame1, bg='white', fg='#107db2')
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
        
        # Entrada de Nome:
        self.lb_nome = Label(self.frame1, text='NOME', bg='#dfe3ee', fg='#107db2')   
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.nome_entry = Entry(self.frame1, bg='white', fg='#107db2')
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.80)
        
        # Entrada de Contato:
        self.lb_nome = Label(self.frame1, text='TELEFONE', bg='#dfe3ee', fg='#107db2')   
        self.lb_nome.place(relx=0.05, rely=0.6)
        self.nome_entry = Entry(self.frame1, bg='white', fg='#107db2')
        self.nome_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        
        # Entrada de Endereço:
        self.lb_nome = Label(self.frame1, text='ENDEREÇO', bg='#dfe3ee', fg='#107db2')   
        self.lb_nome.place(relx=0.5, rely=0.6)
        self.nome_entry = Entry(self.frame1, bg='white', fg='#107db2')
        self.nome_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
        
        
# Chamando a Função:        
App()