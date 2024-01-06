from tkinter import *
from clientes import *
from functools import partial
from order import *

class   Tables(Frame):

    def __init__(self, all_orders, master=NONE):
        super().__init__(master, bg='#A71DF2', bd=2, relief='ridge', width=1000, height=400)
        self.master = master
        self.pack(fill='both')
        self.create_widgets_tables()
        self.all_orders = all_orders


    def abrir_pedido(name, self.all_orders):
        new_order = Order(name)
        self.all_orders.append(new_order)


    def create_widgets_tables(self):
        self.clients = Clients()
        self.list_clients_sorted = sorted(self.clients.list_clients)
        # self.frame_principal = Frame(self)
        # self.frame_principal.pack(expand=True, fill="both")
        # self.frames = [[Frame() for _ in range(5)] for _ in range(6)]
        # n = 0
        # for i in range(6):
        #     for j in range(5):
        #         self.frames[i][j].configure(bg="lightblue")  # Configurar color de fondo
        #         self.frames[i][j].grid(row=i, column=j, padx=5, pady=5, sticky="nsew")  # Posicionar en la grilla
        #         self.frame_principal.grid_rowconfigure(i, weight=1)  # Proporcionar peso a las filas para la expansión uniforme
        #         self.frame_principal.grid_columnconfigure(j, weight=1)  # Proporcionar peso a las columnas para la expansión uniforme
        #         self.b0 = Button(self.frames[i][j], text=list_clients_sorted[n], command=(self.abrir_pedido))
        #         self.b0.pack()
        #         n = n + 1
        # number_clients = len(self.clients.list_clients)
        self.frame_ext_1 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_1.pack(expand=True, fill='x')
        for i in range (5):
            self.f0 = Frame(self.frame_ext_1)
            self.f0.pack(side='left', expand=True, fill='both')
            self.f0.config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.b0 = Button(self.f0, text=self.list_clients_sorted[i], command=partial(self.abrir_pedido, self.list_clients_sorted[i], self.all_orders))
            self.b0.grid(row=0, column=0)
            self.f0.grid_rowconfigure(0, weight=1)
            self.b0.config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.frame_ext_2 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_2.pack(expand=True, fill='x')
        for i in range (5):
            self.f0 = Frame(self.frame_ext_2)
            self.f0.pack(side='left', expand=True, fill='both')
            self.f0.config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.b0 = Button(self.f0, text=self.list_clients_sorted[i + 5], command=(self.abrir_pedido))
            self.b0.grid(row=0, column=0)
            self.f0.grid_rowconfigure(0, weight=1)
            self.b0.config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.frame_ext_3 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_3.pack(expand=True, fill='x')
        for i in range (5):
            self.f0 = Frame(self.frame_ext_3)
            self.f0.pack(side='left', expand=True, fill='both')
            self.f0.config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.b0 = Button(self.f0, text=self.list_clients_sorted[i + 10], command=(self.abrir_pedido))
            self.b0.grid(row=0, column=0)
            self.f0.grid_rowconfigure(0, weight=1)
            self.b0.config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.frame_ext_4 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_4.pack(expand=True, fill='x')
        for i in range (5):
            self.f0 = Frame(self.frame_ext_4)
            self.f0.pack(side='left', expand=True, fill='both')
            self.f0.config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.b0 = Button(self.f0, text=self.list_clients_sorted[i + 15], command=(self.abrir_pedido))
            self.b0.grid(row=0, column=0)
            self.f0.grid_rowconfigure(0, weight=1)
            self.b0.config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.frame_ext_5 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_5.pack(expand=True, fill='x')
        for i in range (5):
            self.f0 = Frame(self.frame_ext_5)
            self.f0.pack(side='left', expand=True, fill='both')
            self.f0.config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.b0 = Button(self.f0, text=self.list_clients_sorted[i + 20], command=(self.abrir_pedido))
            self.b0.grid(row=0, column=0)
            self.f0.grid_rowconfigure(0, weight=1)
            self.b0.config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.frame_ext_6 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_6.pack(expand=True, fill='x')
        for i in range (5):
            self.f0 = Frame(self.frame_ext_6)
            self.f0.pack(side='left', expand=True, fill='both')
            self.f0.config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.b0 = Button(self.f0, text=self.list_clients_sorted[i + 25], command=(self.abrir_pedido))
            self.b0.grid(row=0, column=0)
            self.f0.grid_rowconfigure(0, weight=1)
            self.b0.config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)

    # def abrir_pedido():
    #     pass

    def abrir_pedido_nuevo_cliente():
        pass