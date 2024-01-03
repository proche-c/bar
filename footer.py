from tkinter import *

class Footer(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=40)
        self.master = master
        self.pack(anchor='n', fill='both')
        self.config(bg='#525252')
        self.create_widgets()

    def create_widgets(self):
        self.version = Frame(self)
        self.version.pack(side='left', fill='y')
        self.version.config(bg = '#9A6FE0', width=500, height=40)
        self.v = Label(self.version, bg = '#9A6FE0', text= "bar Anadon v1.0")
        self.v.pack(anchor='center', fill='both')
        self.v.config(bg='#525252', font=("Verdana", 16), padx=8)
        self.author = Frame(self)
        self.author.pack(side='right', fill='y')
        self.author.config(bg = '#9A6FE0', width=500, height=40)
        self.a = Label(self.author, bg = '#9A6FE0', text= "desarrollado por Paula Roche Castro")
        self.a.pack(fill='both')
        self.a.config(bg='#525252', font=("Verdana", 16), padx=8)
    