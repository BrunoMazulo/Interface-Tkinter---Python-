from tkinter import *
from tkinter import ttk

root = Tk()

class Functions():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)


class Application(Functions):
    def __init__(self):
        # This is the principal function, it call all functions about interface
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes") # Title window
        self.root.configure(background='#1e3743') # Background color window
        self.root.geometry("700x500")
        self.root.resizable(True, True) # False, False -> Fixed window axis x and y // True, True -> Responsible
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)
    
    def frame_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        # bd=border / bg=background / highlightbackground=border_color / highlightthickness=border_large
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth=0.96, relheight=0.46) 
        # relx/7 -> margin,position (percent) // relwidth/height -> 0 until 1 in pencent (0.96 = 96% widht, 0.5 = 46% height)
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth=0.96, relheight=0.46) #rely=0.5 [50%] from top 
    
    def widgets_frame1(self):

        ## Creating buttons
        # Cleanner button
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg='#187db2', fg='white', font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.02,relwidth=0.1, relheight=0.15)
        # Find Button
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg='#187db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.02,relwidth=0.1, relheight=0.15)
        # New User Button
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#187db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_novo.place(relx=0.6, rely=0.02,relwidth=0.1, relheight=0.15)
        # Update User Button
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg='#187db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.02,relwidth=0.1, relheight=0.15)
        # Delete User Button
        self.bt_excluir = Button(self.frame_1, text="Excluir", bd=2, bg='#FF9079', fg='white', font=('verdana', 8, 'bold'))
        self.bt_excluir.place(relx=0.8, rely=0.02,relwidth=0.1, relheight=0.15)
        
        ## Creating Label and Input - Código -
        self.lb_codigo = Label(self.frame_1, text="Código", bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05,)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ## Creating Label and Input - Nome -
        self.lb_nome = Label(self.frame_1, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35,)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## Creating Label and Input - Telefone -
        self.lb_telefone = Label(self.frame_1, text="Telefone", bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.6,)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Creating Label and Input - Cidade -
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6,)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        self.lista_clientes = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4")) 
        self.lista_clientes.heading("#0", text="")
        self.lista_clientes.heading("#1", text="Código")
        self.lista_clientes.heading("#2", text="Nome")
        self.lista_clientes.heading("#3", text="Telefone")
        self.lista_clientes.heading("#4", text="Cidade")

        self.lista_clientes.column("#0", width=1)
        self.lista_clientes.column("#1", width=50)
        self.lista_clientes.column("#2", width=200)
        self.lista_clientes.column("#3", width=125)
        self.lista_clientes.column("#4", width=125)

        self.lista_clientes.place(relx=0.01,rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroollista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_clientes.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

Application()
# Funcs()