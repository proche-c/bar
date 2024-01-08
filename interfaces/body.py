from tkinter import *
from interfaces.mesas import *
from interfaces.pedidos import *
from interfaces.administracion import *
from functools import partial

class Body(Frame):

    def __init__(self, all_orders, clients, catalogue, master=NONE):
        super().__init__(master, width=1000, height=400)
        self.master = master
        self.pack(fill='both')
        self.config(bg='#ECE8F7')
        self.active_pedidos = 0
        self.active_adcion = 0
        self.create_widgets(all_orders, clients, catalogue)

    def create_widgets(self, all_orders, clients, catalogue):
        self.create_instances_subwindows(all_orders, clients)
        self.create_menu(all_orders, clients, catalogue)

    def create_instances_subwindows(self, all_orders, clients):
        self.p = WindowOrders(all_orders, self)
        self.a = WindowAdcion(all_orders, self)
        pr = WindowProducts(all_orders, self)
        self.pr = pr
        self.t = WindowTables(all_orders, clients, pr, self)
    
    def create_menu(self, all_orders, clients, catalogue):
        # Esto es el frame principal donde van los botones
        self.menu = Frame(self)
        self.menu.pack(expand=True, fill='x')
        self.menu.config(bg='#75BCE6', bd=2, relief='ridge', height=80)

        # ***********  PEDIDOS   *************
        # Esto es el frame donde va el boton de pedidos
        self.frame_pedidos = Frame(self.menu)
        self.frame_pedidos.pack(side='left', fill='both', expand=True)
        self.frame_pedidos.config(bg='#75BCE6', bd=2, relief='ridge', padx=20, pady=10)

        # Esto es el boton de pedidos
        self.button_pedidos = Button(self.frame_pedidos, text='PEDIDOS', command=self.mostrar_pedidos)
        self.button_pedidos.grid(row=0, column=0)
        self.frame_pedidos.grid_rowconfigure(0, weight=1)
        self.button_pedidos.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

        # ***********  MESAS   *************
        # Esto es el frame donde va el boton de mesas
        self.frame_mesas = Frame(self.menu)
        self.frame_mesas.pack(side='left', fill='both', expand=True)
        self.frame_mesas.config(bg='#75BCE6', bd=2, relief='ridge', padx=20, pady=10)

        # Esto es el boton de mesas
        self.button_mesas = Button(self.frame_mesas, text='MESAS', command=partial(self.mostrar_mesas, all_orders, clients))
        self.button_mesas.grid(row=0, column=0)
        self.frame_mesas.grid_rowconfigure(0, weight=1)
        self.button_mesas.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

        # ***********  PRODUCTOS   *************
        # Esto es el frame donde va el boton de productos
        self.frame_productos = Frame(self.menu)
        self.frame_productos.pack(side='left', fill='both', expand=True)
        self.frame_productos.config(bg='#75BCE6', bd=2, relief='ridge', padx=20, pady=10)

        # Esto es el boton de mesas
        self.button_productos = Button(self.frame_productos, text='PRODUCTOS',command=partial(self.mostrar_productos, all_orders))
        self.button_productos.grid(row=0, column=0)
        self.frame_productos.grid_rowconfigure(0, weight=1)
        self.button_productos.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

        
         # ***********  PANEL DE ADMINISTRACION   *************
        # Esto es el frame donde va el boton de panel de administracion
        self.frame_adcion = Frame(self.menu)
        self.frame_adcion.pack(side='left', fill='both', expand=True)
        self.frame_adcion.config(bg='#75BCE6', bd=2, relief='ridge', padx=20, pady=10)

        # Esto es el boton de panel de administracion
        self.button_adcion = Button(self.frame_adcion, text='PANEL DE ADMINISTRACION', command=self.mostrar_adcion)
        self.button_adcion.grid(row=0, column=0)
        self.frame_adcion.grid_rowconfigure(0, weight=1)
        self.button_adcion.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

        self.blank = Frame(self, bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=400)
        self.blank.pack(fill='both')
        self.blank.config(bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=460)

 

    def mostrar_pedidos(self):
        self.blank.pack_forget()
        if self.t.window_is_active == 1:
            self.t.pack_forget()
            self.t.destroy_widgets_tables()
            self.t.window_is_active = 0
        if self.pr.window_is_active == 1:
            self.pr.pack_forget()
            self.pr.window_is_active = 0
        if self.a.window_is_active == 1:
            self.a.pack_forget()
            self.a.window_is_active = 0
        #self.window_pedidos = Frame(self, bg='#F21D7D', bd=2, relief='ridge', width=1000, height=400)
        self.p.pack(fill='both')
        self.p.print_prueba()
        self.p.window_is_active = 1

    def mostrar_mesas(self, all_orders, clients):
        self.blank.pack_forget()
        if self.p.window_is_active == 1:
            self.p.pack_forget()
            self.p.window_is_active = 0
        if self.pr.window_is_active == 1:
            self.pr.pack_forget()
            self.pr.window_is_active = 0
        if self.a.window_is_active == 1:
            self.a.pack_forget()
            self.a.window_is_active = 0
        #self.t = WindowTables(all_orders, clients, self)
        self.t.pack(fill='both')
        self.t.create_widgets_tables(all_orders, clients)
        self.t.window_is_active = 1


    def mostrar_productos(self, all_orders):
        self.blank.pack_forget()
        if self.t.window_is_active == 1:
            self.t.pack_forget()
            self.t.destroy_widgets_tables()
            self.t.window_is_active = 0
        if self.p.window_is_active == 1:
            self.p.pack_forget()
            self.p.window_is_active = 0
        if self.a.window_is_active == 1:
            self.a.pack_forget()
            self.a.window_is_active = 0
        self.pr.pack(fill='both')
        self.pr.window_is_active = 1

    def mostrar_adcion(self):
        self.blank.pack_forget()
        if self.t.window_is_active == 1:
            self.t.pack_forget()
            self.t.destroy_widgets_tables()
            self.t.window_is_active = 0
        if self.p.window_is_active == 1:
            self.p.pack_forget()
            self.p.window_is_active = 0
        if self.pr.window_is_active == 1:
            self.pr.pack_forget()
            self.pr.window_is_active = 0
        #self.window_adcion = Frame(self, bg='#86F556', bd=2, relief='ridge', width=1000, height=400)
        self.a.pack(fill='both')
        self.a.window_is_active = 1