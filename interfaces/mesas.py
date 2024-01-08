from tkinter import *
from clases.clientes import *
from functools import partial
from clases.order import *
from interfaces.productos import *

class   WindowTables(Frame):

    def __init__(self, all_orders, clients, pr, master=NONE):
        super().__init__(master, bg='#A71DF2', bd=2, relief='ridge', width=1000, height=400)
        self.master = master
        self.all_orders = all_orders
        self.clients = clients
        self.active_client = ""
        self.window_is_active = 0
        self.pr = pr


    def set_pedido_active(self, name, all_orders):
        self.active_client = name
        new_order = Order(name)
        if self.all_orders.add_order(new_order) == 0:
            print("se ha añadido el pedido")
            print(new_order.client)
            self.all_orders.order_runing = new_order
        else:
            self.all_orders.order_runing = self.all_orders.find_order_by_client(name)   
        self.pack_forget()
        self.window_is_active = 0
        self.destroy_widgets_tables()
        self.pr.pack()
        self.pr.window_is_active = 1


    def create_widgets_tables(self, all_orders, clients):
        self.list_clients_sorted = sorted(clients.list_clients)
        #print(self.list_clients_sorted)
        self.F1 = ["f1", "f2", "f3", "f4", "f5"]
        self.B1 = ["b1", "b2", "b3", "b4", "b5"]
        self.frame_ext_1 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_1.pack(expand=True, fill='x')
        for i in range (5):
            self.F1[i] = Frame(self.frame_ext_1)
            self.F1[i].pack(side='left', expand=True, fill='both')
            self.F1[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.B1[i] = Button(self.F1[i], text=self.list_clients_sorted[i], command=partial(self.set_pedido_active, self.list_clients_sorted[i], all_orders))
            self.B1[i].grid(row=0, column=0)
            self.F1[i].grid_rowconfigure(0, weight=1)
            self.B1[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.F2 = ["f6", "f7", "f8", "f9", "f10"]
        self.B2 = ["b6", "b7", "b8", "b9", "b10"]
        self.frame_ext_2 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_2.pack(expand=True, fill='x')
        for i in range (5):
            self.F2[i] = Frame(self.frame_ext_2)
            self.F2[i].pack(side='left', expand=True, fill='both')
            self.F2[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.B2[i] = Button(self.F2[i], text=self.list_clients_sorted[i + 5], command=partial(self.set_pedido_active, self.list_clients_sorted[i + 5], all_orders))
            self.B2[i].grid(row=0, column=0)
            self.F2[i].grid_rowconfigure(0, weight=1)
            self.B2[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.F3 = ["f11", "f12", "f13", "f14", "f15"]
        self.B3 = ["b11", "b12", "b13", "b14", "b15"]
        self.frame_ext_3 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_3.pack(expand=True, fill='x')
        for i in range (5):
            self.F3[i] = Frame(self.frame_ext_3)
            self.F3[i].pack(side='left', expand=True, fill='both')
            self.F3[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.B3[i] = Button(self.F3[i], text=self.list_clients_sorted[i + 10], command=partial(self.set_pedido_active, self.list_clients_sorted[i + 10], all_orders))
            self.B3[i].grid(row=0, column=0)
            self.F3[i].grid_rowconfigure(0, weight=1)
            self.B3[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.F4 = ["f16", "f17", "f18", "f19", "f20"]
        self.B4 = ["b16", "b17", "b18", "b19", "b20"]
        self.frame_ext_4 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_4.pack(expand=True, fill='x')
        for i in range (5):
            self.F4[i] = Frame(self.frame_ext_4)
            self.F4[i].pack(side='left', expand=True, fill='both')
            self.F4[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.B4[i] = Button(self.F4[i], text=self.list_clients_sorted[i + 15], command=partial(self.set_pedido_active, self.list_clients_sorted[i + 15], all_orders))
            self.B4[i].grid(row=0, column=0)
            self.F4[i].grid_rowconfigure(0, weight=1)
            self.B4[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.F5 = ["f21", "f22", "f23", "f24", "f25"]
        self.B5 = ["b21", "b22", "b23", "b24", "b25"]
        self.frame_ext_5 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_5.pack(expand=True, fill='x')
        for i in range (5):
            self.F5[i] = Frame(self.frame_ext_5)
            self.F5[i].pack(side='left', expand=True, fill='both')
            self.F5[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.B5[i] = Button(self.F5[i], text=self.list_clients_sorted[i + 20], command=partial(self.set_pedido_active, self.list_clients_sorted[i + 20], all_orders))
            self.B5[i].grid(row=0, column=0)
            self.F5[i].grid_rowconfigure(0, weight=1)
            self.B5[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.F6 = ["f26", "f27", "f28", "f29", "f30"]
        self.B6 = ["b26", "b27", "b28", "b29", "b30"]
        self.frame_ext_6 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_6.pack(expand=True, fill='x')
        for i in range (5):
            self.F6[i] = Frame(self.frame_ext_6)
            self.F6[i].pack(side='left', expand=True, fill='both')
            self.F6[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.B6[i] = Button(self.F6[i], text=self.list_clients_sorted[i + 25], command=partial(self.set_pedido_active, self.list_clients_sorted[i + 25], all_orders))
            self.B6[i].grid(row=0, column=0)
            self.F6[i].grid_rowconfigure(0, weight=1)
            self.B6[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)

    def destroy_widgets_tables(self):
        for i in range(5):
            self.B1[i].destroy()
            self.F1[i].destroy()
            self.B2[i].destroy()
            self.F2[i].destroy()
            self.B3[i].destroy()
            self.F3[i].destroy()
            self.B4[i].destroy()
            self.F4[i].destroy()
            self.B5[i].destroy()
            self.F5[i].destroy()
            self.B6[i].destroy()
            self.F6[i].destroy()
        self.frame_ext_1.destroy()
        self.frame_ext_2.destroy()
        self.frame_ext_3.destroy()
        self.frame_ext_4.destroy()
        self.frame_ext_5.destroy()
        self.frame_ext_6.destroy()























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
        #         self.B3[i] = Button(self.frames[i][j], text=list_clients_sorted[n], command=(self.abrir_pedido))
        #         self.B3[i].pack()
        #         n = n + 1
        # number_clients = len(self.clients.list_clients)