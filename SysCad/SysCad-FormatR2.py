from tkinter import*
from tkinter import ttk


root=Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.tel_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.cnpj_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

class Application(Funcs):
    def __init__(self):
        
        self.root=root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()
      
        
    def tela(self):
       
        self.root.title("::: SYSCAD ::: FORMAT.R2 :::")
        self.root.configure(background="#000000")
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=900,height=700)
        self.root.minsize(width=500, height=400)


    def frames_da_tela(self):
        
        self.frame_1=Frame(self.root, bd=4, bg="lightcyan", highlightbackground="gray", highlightthickness=4)
        self.frame_1.place(relx=0.02,rely=0.02, relwidth=0.96, relheight=0.46)


        self.frame_2=Frame(self.root, bd=4, bg="lightcyan", highlightbackground="gray", highlightthickness=4)
        self.frame_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.46)


    def widgets_frame1(self):
        self.bt_limpar=Button(self.frame_1, text="Limpar",bd=3, bg="white", fg="black", font=("verdana",8,"bold"), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar=Button(self.frame_1, text="Buscar", bd=3,bg="#107db2", fg="white", font=("verdana",8,"bold"))
        self.bt_buscar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)


        self.bt_buscar=Button(self.frame_1, text="Novo", bd=3, bg="cadetblue3", fg="white", font=("verdana",8,"bold"))
        self.bt_buscar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)


        self.bt_buscar=Button(self.frame_1, text="Alterar",bd=3, bg="#107db2", fg="white", font=("verdana",8,"bold"))
        self.bt_buscar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)


        self.bt_buscar=Button(self.frame_1, text="Apagar", bd=3, bg="tomato", fg="white", font=("verdana",8,"bold"))
        self.bt_buscar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # criaçao da label e entrada do codigo

        self.lb_codigo=Label(self.frame_1, text="::: Código :::", bg="lightcyan", fg="black")
        self.lb_codigo.place(relx=0.06, rely= 0.07)

        self.codigo_entry=Entry(self.frame_1,bg="ivory2", foreground='black')
        self.codigo_entry.place(relx=0.07, rely=0.15,relwidth=0.07)

        # criacao da label e entrada do nome

        self.lb_nome=Label(self.frame_1, text="::: Nome :::", bg="lightcyan", fg="black")
        self.lb_nome.place(relx=0.07, rely= 0.35)

        self.nome_entry=Entry(self.frame_1,bg="ivory2", foreground='black')
        self.nome_entry.place(relx=0.07, rely=0.45,relwidth=0.4)


        # criacao da label e entrada do E-mail

        self.lb_email=Label(self.frame_1, text="::: E-mail :::", bg="lightcyan", fg="black")
        self.lb_email.place(relx=0.5, rely= 0.35)

        self.email_entry=Entry(self.frame_1,bg="ivory2", foreground='black')
        self.email_entry.place(relx=0.5, rely=0.45,relwidth=0.3)


        #criacao da label e entrada do telefone

        self.lb_tel=Label(self.frame_1, text="::: Telefone :::", bg="lightcyan", fg="black")
        self.lb_tel.place(relx=0.07, rely= 0.6)

        self.tel_entry=Entry(self.frame_1,bg="ivory2", foreground='black')
        self.tel_entry.place(relx=0.07, rely=0.7,relwidth=0.2)

        #criacao da label e entrada do cep

        self.lb_cep=Label(self.frame_1, text="::: CEP :::", bg="lightcyan", fg="black")
        self.lb_cep.place(relx=0.3, rely= 0.6)

        self.cep_entry=Entry(self.frame_1,bg="ivory2", foreground='black')
        self.cep_entry.place(relx=0.3, rely=0.7,relwidth=0.2)

        #criacao da label e entrada do CNPJ

        self.lb_cnpj=Label(self.frame_1, text="::: CNPJ :::", bg="lightcyan", fg="black")
        self.lb_cnpj.place(relx=0.56, rely= 0.6)

        self.cnpj_entry=Entry(self.frame_1,bg="ivory2", foreground='black')
        self.cnpj_entry.place(relx=0.56, rely=0.7,relwidth=0.2)


        #criacao da label e entrada da cidade

        self.lb_cidade=Label(self.frame_1, text="::: Cidade :::", bg="lightcyan", fg="black")
        self.lb_cidade.place(relx=0.8, rely= 0.6)

        self.cidade_entry=Entry(self.frame_1,bg="ivory2", foreground='black')
        self.cidade_entry.place(relx=0.8, rely=0.7,relwidth=0.2)


    def lista_frame2(self):
        self.listacli=ttk.Treeview(self.frame_2,height=3,column=("coluna1", "coluna2", "coluna3", "coluna4"))
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="CÓDIGO")
        self.listacli.heading("#2", text="NOME")
        self.listacli.heading("#3", text="TELEFONE")
        self.listacli.heading("#4", text="CIDADE")
        
        self.listacli.column("#0", width=1)
        self.listacli.column("#1", width=50)
        self.listacli.column("#2", width=200)
        self.listacli.column("#3", width=125)
        self.listacli.column("#4", width=125)

        self.listacli.place(relx=0.01,rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista= Scrollbar(self.frame_2, orient="vertical")
        self.listacli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96,rely=0.1,relwidth=0.04,relheight=0.85)
        
Application()