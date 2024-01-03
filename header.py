from tkinter import *

class Header(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=60)
        self.master = master
        self.pack(anchor='n', fill='both')
        self.config(bg='#75BCE6')
        self.create_widgets()

    def create_widgets(self):
        self.title = Frame(self)
        self.title.pack(side='left', fill='y')
        self.title.config(bg='#75BCE6', width=300, height=60, padx=20, pady=10)
        self.t = Label(self.title, bg='#75BCE6', text='BAR ANADON')
        self.t.pack(side='left', fill='both')
        self.t.config(bg='#75BCE6', font=("Verdana", 16, "bold"), padx=12, fg='#2B2B2B')