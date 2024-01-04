from tkinter import *
import datetime

class Header(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=70)
        self.master = master
        self.pack(fill='x')
        self.config(bg='#75BCE6', bd=2, relief='ridge')
        self.initial_date = datetime.datetime.now()
        self.create_widgets()

    def create_widgets(self):
        #aqui falta que se vaya actualizando la hora
        self.title = Frame(self)
        self.title.pack(side='left', fill='y')
        self.title.config(bg='#75BCE6', width=500, height=60, padx=50, pady=4)
        self.t = Label(self.title, bg='#75BCE6', text='BAR ANADON')
        self.t.pack(fill='both')
        self.t.config(bg='#75BCE6', font=("Verdana", 16, "bold"), fg='#2B2B2B')
        self.date = Frame(self)
        self.date.pack(side='left', fill='y')
        self.date.config(bg='#75BCE6', width=500, height=60, padx=50, pady=4)
        self.d = Label(self.date, bg='#75BCE6', text= self.initial_date.strftime("%A %d %B %Y %I:%M"))
        self.d.pack(fill='both')
        self.d.config(bg='#75BCE6', font=("Verdana", 16, "bold"), fg='#2B2B2B')
  