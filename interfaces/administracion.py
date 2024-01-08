from tkinter import *

class   WindowAdcion(Frame):

    def __init__(self, all_orders, master=NONE):
        super().__init__(master, bg='#86F556', bd=2, relief='ridge', width=1000, height=400)
        self.master = master
        self.window_is_active = 0