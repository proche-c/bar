from tkinter import *

class Body(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=510)
        self.master = master
        self.pack(anchor='n', fill='both')
        self.config(bg='#ECE8F7')