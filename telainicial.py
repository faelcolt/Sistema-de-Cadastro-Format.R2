from tkinter import *

root = Tk()

class aplication():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title('CADASTRO DE CLIENTES')
        self.root.configure(background='#1e3743')
        self.root.geometry('788x588')
        self.root.resizable(True, True)
        self.root.maxsize(width=988, height=788)
        self.root.minsize(width=550, height=550)

aplication()