from tkinter import *

class   WindowProducts(Frame):

    def __init__(self, all_orders, master=NONE):
        super().__init__(master, bg='#C7E0BC', bd=2, relief='ridge', width=1000, height=400)
        self.master = master
        self.window_is_active = 0
        #self.pack(fill='both')