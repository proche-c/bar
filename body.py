from tkinter import *

class Body(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=400)
        self.master = master
        self.pack(fill='both')
        self.config(bg='#ECE8F7')
        self.active_pedidos = 0
        self.active_mesas = 0
        self.active_adcion = 0
        self.create_widgets()


    def create_widgets(self):
        self.create_menu()

    def create_menu(self):

        # Esto es el frame principal donde van los botones
        self.menu = Frame(self)
        self.menu.pack(fill='x')
        self.menu.config(bg='#75BCE6', bd=2, relief='ridge', width=1000, height=80)

       
        # ***********  PEDIDOS   *************
        # Esto es el frame donde va el boton de pedidos
        self.frame_pedidos = Frame(self.menu)
        self.frame_pedidos.pack(side='left', fill='y')
        self.frame_pedidos.config(bg='#75BCE6', bd=2, relief='ridge', width=300, height=80, padx=80, pady=10)

        # Esto es el boton de pedidos
        self.button_pedidos = Button(self.frame_pedidos, text='PEDIDOS', command=self.mostrar_pedidos)
        self.button_pedidos.grid(row=0, column=0)
        self.frame_pedidos.grid_rowconfigure(0, weight=1)
        self.button_pedidos.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

       
        # ***********  MESAS   *************
        # Esto es el frame donde va el boton de mesas
        self.frame_mesas = Frame(self.menu)
        self.frame_mesas.pack(side='left', fill='y')
        self.frame_mesas.config(bg='#75BCE6', bd=2, relief='ridge', width=300, height=80, padx=80, pady=10)

        # Esto es el boton de mesas
        self.button_mesas = Button(self.frame_mesas, text='MESAS', command=self.mostrar_mesas)
        self.button_mesas.grid(row=0, column=0)
        self.frame_mesas.grid_rowconfigure(0, weight=1)
        self.button_mesas.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

        
         # ***********  PANEL DE ADMINISTRACION   *************
        # Esto es el frame donde va el boton de panel de administracion
        self.frame_adcion = Frame(self.menu)
        self.frame_adcion.pack(side='left', fill='y')
        self.frame_adcion.config(bg='#75BCE6', bd=2, relief='ridge', width=395, height=80, padx=80, pady=10)

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
        if self.active_mesas == 1:
            self.window_mesas.pack_forget()
            self.active_mesas = 0
        if self.active_adcion == 1:
            self.window_adtion.pack_forget()
            self.active_adcion = 0
        self.window_pedidos = Frame(self, bg='#F21D7D', bd=2, relief='ridge', width=1000, height=400)
        self.window_pedidos.pack(fill='both')
        self.active_pedidos = 1

    def mostrar_mesas(self):
        self.blank.pack_forget()
        if self.active_pedidos == 1:
            self.window_pedidos.pack_forget()
            self.active_pedidos = 0
        if self.active_adcion == 1:
            self.window_adtion.pack_forget()
            self.active_adcion = 0
        self.window_mesas = Frame(self, bg='#A71DF2', bd=2, relief='ridge', width=1000, height=400)
        self.window_mesas.pack(fill='both')
        self.active_mesas = 1

    def mostrar_adcion(self):
        self.blank.pack_forget()
        if self.active_mesas == 1:
            self.window_mesas.pack_forget()
            self.active_mesas = 0
        if self.active_adcion == 1:
            self.window_adtion.pack_forget()
        self.window_adcion = Frame(self, bg='#86F556', bd=2, relief='ridge', width=1000, height=400)
        self.window_adcion.pack(fill='both')
        self.active_adcion = 1