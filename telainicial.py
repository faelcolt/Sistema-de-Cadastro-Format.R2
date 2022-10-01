from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
    def tela(self):
        self.root.title('CADASTRO DE CLIENTES')
        self.root.configure(background='#1e3743')
        self.root.geometry('788x588')
        self.root.resizable(True, True)
        self.root.maxsize(width=988, height=788)
        self.root.minsize(width=400, height=300)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6')
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

Application()