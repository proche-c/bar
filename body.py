from tkinter import *

class Body(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=400)
        self.master = master
        self.pack(fill='both')
        self.config(bg='#ECE8F7')
        self.create_widgets()

    def abrir_pedidos(self):
        self.screen_pedidos = Frame(self.blank)
        self.screen_pedidos.pack(anchor='n', fill='y')
        self.screen_pedidos.config(bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=400)
        self.label_prueba_pedidos = Label(self.screen_pedidos, text='PPPEDIDOS')
        self.label_prueba_pedidos.pack()

    def abrir_mesas(self):
        self.screen_mesas = Frame(self.blank)
        self.screen_mesas.pack(anchor='n', fill='y')
        self.screen_mesas.config(bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=400)
        self.label_prueba_mesas = Label(self.screen_pedidos, text='MESASSS')
        self.label_prueba_mesas.pack()

    def create_widgets(self):
        self.create_menu()
        self.create_blank()

    def create_menu(self):

        self.menu = Frame(self)
        self.menu.pack(fill='both')
        self.menu.config(bg='#75BCE6', bd=2, relief='ridge', width=1000, height=80)


        self.button_pedidos = Button(self.menu, text='PEDIDOS', command=self.abrir_pedidos)
        self.button_pedidos.grid(row=0, column=0, sticky='w')
        self.button_pedidos.config(font=("Verdana", 16), bg='#75BCE6', padx=20, pady=5)


        self.button_mesas = Button(self.menu, text='MESAS', command=self.abrir_mesas)
        self.button_mesas.grid(row=0, column=1)
        self.button_mesas.config(font=("Verdana", 16), bg='#75BCE6', padx=20, pady=5)
  

        self.button_administracion = Button(self.menu, text='PANEL DE ADMINISTRACION', command=self.abrir_mesas)
        self.button_administracion.grid(row=0, column=2, sticky='e')
        self.button_administracion.config(font=("Verdana", 16), bg='#75BCE6', padx=20, pady=5)

    def create_blank(self):
        self.blank = Frame(self, bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=400)
        self.blank.place(x=0, y=140)
        #self.blank.config(bg='#F2F7F8', bd=2, relief='ridge', width=1000, height=400)   
