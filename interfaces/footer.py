from tkinter import *

class Footer(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=20)
        self.master = master
        self.pack(anchor='s', fill='x')
        self.config(bg='#525252')
        self.create_widgets()

    def create_widgets(self):
        self.version = Frame(self)
        self.version.pack(side='left', fill='x')
        self.version.config(bg = '#9A6FE0', width=500, height=20)
        self.v = Label(self.version, bg = '#9A6FE0', text= "bar Anadon v1.0")
        self.v.pack(anchor='center', fill='x')
        self.v.config(bg='#525252', font=("Verdana", 16), padx=8)
        self.author = Frame(self)
        self.author.pack(side='right', fill='x')
        self.author.config(bg = '#9A6FE0', width=500, height=20)
        self.a = Label(self.author, bg = '#9A6FE0', text= "desarrollado por Paula Roche Castro")
        self.a.pack(fill='x')
        self.a.config(bg='#525252', font=("Verdana", 16), padx=8)
    