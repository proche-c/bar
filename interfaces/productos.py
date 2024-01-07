from tkinter import *

class   WindowProducts(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, bg='#C7E0BC', bd=2, relief='ridge', width=1000, height=400)
        self.master = master
        self.pack(fill='both')