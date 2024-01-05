from tkinter import *

class Body(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=400)
        self.master = master
        self.pack(fill='both')
        self.config(bg='#ECE8F7')
        self.create_widgets()

    def abrir_pedidos(self):
        pass
        # self.screen_pedidos = Frame(self.blank)
        # self.screen_pedidos.pack(anchor='n', fill='y')
        # self.screen_pedidos.config(bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=400)
        # self.label_prueba_pedidos = Label(self.screen_pedidos, text='PPPEDIDOS')
        # self.label_prueba_pedidos.pack()

    def abrir_mesas(self):
        pass
        # self.screen_mesas = Frame(self.blank)

        # self.screen_mesas.pack(anchor='n', fill='both')
        # self.screen_mesas.config(bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=400)
        # self.label_prueba_mesas = Label(self.screen_pedidos, text='MESASSS')
        # self.label_prueba_mesas.pack()

    def create_widgets(self):
        self.create_menu()
        self.create_blank()

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
        self.button_pedidos = Button(self.frame_pedidos, text='PEDIDOS', command=self.abrir_pedidos)
        self.button_pedidos.grid(row=0, column=0)
        self.frame_pedidos.grid_rowconfigure(0, weight=1)
        self.button_pedidos.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

       
        # ***********  MESAS   *************
        # Esto es el frame donde va el boton de mesas
        self.frame_mesas = Frame(self.menu)
        self.frame_mesas.pack(side='left', fill='y')
        self.frame_mesas.config(bg='#75BCE6', bd=2, relief='ridge', width=300, height=80, padx=80, pady=10)

        # Esto es el boton de mesas
        self.button_mesas = Button(self.frame_mesas, text='MESAS', command=self.abrir_pedidos)
        self.button_mesas.grid(row=0, column=0)
        self.frame_mesas.grid_rowconfigure(0, weight=1)
        self.button_mesas.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

        
         # ***********  PANEL DE ADMINISTRACION   *************
        # Esto es el frame donde va el boton de panel de administracion
        self.frame_adcion = Frame(self.menu)
        self.frame_adcion.pack(side='left', fill='y')
        self.frame_adcion.config(bg='#75BCE6', bd=2, relief='ridge', width=395, height=80, padx=80, pady=10)

        # Esto es el boton de panel de administracion
        self.button_adcion = Button(self.frame_adcion, text='PANEL DE ADMINISTRACION', command=self.abrir_pedidos)
        self.button_adcion.grid(row=0, column=0)
        self.frame_adcion.grid_rowconfigure(0, weight=1)
        self.button_adcion.config(font=("Verdana", 16), bg='#75BCE6', padx=4, pady=4)

    def create_blank(self):
        self.blank = Frame(self, bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=400)
        self.blank.pack(fill='both')
        self.blank.config(bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=460)   
