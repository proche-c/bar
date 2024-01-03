from tkinter import *
import datetime

class Header(Frame):

    def __init__(self, master=NONE):
        super().__init__(master, width=1000, height=60)
        self.master = master
        self.pack(anchor='n', fill='both')
        self.config(bg='#75BCE6')
        self.current_date = datetime.datetime.now()
        self.current_day = self.current_date.date()
        self.current_time = self.current_date.time()
        self.create_widgets()

    def create_widgets(self):
        self.title = Frame(self)
        self.title.pack(side='left', fill='y')
        self.title.config(bg='#75BCE6', width=300, height=60, padx=20, pady=10)
        self.t = Label(self.title, bg='#75BCE6', text='BAR ANADON')
        self.t.pack(side='left', fill='both')
        self.t.config(bg='#75BCE6', font=("Verdana", 16, "bold"), padx=20, fg='#2B2B2B')
        self.date = Frame(self)
        self.date.pack(side='left', fill='y')
        self.date.config(bg='#75BCE6', width=300, height=60, padx=20, pady=10)
        self.d = Label(self.date, bg='#75BCE6', text= self.current_day)
        self.d.pack(side='left', fill='both')
        self.d.config(bg='#75BCE6', font=("Verdana", 16, "bold"), padx=20, fg='#2B2B2B')
        self.time = Frame(self)
        self.time.pack(side='left', fill='y')
        self.time.config(bg='#75BCE6', width=300, height=60, padx=20, pady=10)
        self.tm = Label(self.time, bg='#75BCE6', text= self.current_time)
        self.tm.pack(side='left', fill='both')
        self.tm.config(bg='#75BCE6', font=("Verdana", 16, "bold"), padx=20, fg='#2B2B2B')