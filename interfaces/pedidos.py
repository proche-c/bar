from tkinter import *

class   WindowOrders(Frame):

    def __init__(self, all_orders, master=NONE):
        super().__init__(master, bg='#F21D7D', bd=2, relief='ridge', width=1000, height=400)
        self.master = master
        self.all_orders = all_orders
        self.window_is_active = 0

    def print_prueba(self):
        print(len(self.all_orders.list_unpaid_orders))
        for order in self.all_orders.list_unpaid_orders:
            print(order.client)