from tkinter import *

class   WindowOrders(Frame):

    def __init__(self, all_orders, master=NONE):
        super().__init__(master, bg='#F21D7D', bd=2, relief='ridge', width=1000, height=400)
        self.master = master
        self.all_orders = all_orders
        self.window_is_active = 0
        #self.create_widgets_orders()

    def print_prueba(self):
        print(len(self.all_orders.list_unpaid_orders))
        for order in self.all_orders.list_unpaid_orders:
            print(order.client)

    def create_widgets_orders(self):
        self.F1 = ["f1", "f2", "f3", "f4", "f5"]
        self.B1 = ["b1", "b2", "b3", "b4", "b5"]
        self.frame_ext_1 = Frame(self, bg='#D7DEE0', height=80)
        self.frame_ext_1.pack(expand=True, fill='x')
        for i in range (5):
            self.F1[i] = Frame(self.frame_ext_1)
            self.F1[i].pack(side='left', expand=True, fill='both')
            self.F1[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.B1[i] = Button(self.F1[i], text="hola", command=self.go_to_order)
            self.B1[i].grid(row=0, column=0)
            self.F1[i].grid_rowconfigure(0, weight=1)
            self.B1[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        # n_frames = len(self.all_orders.list_unpaid_orders)
        # self.orders_frame = Frame(self, bg='#E8E5E6', height=80)
        # self.pack(expand=True, fill='x')
        # self.button_prueba = Button(self.orders_frame, text="pedido prueba", command=self.go_to_order)
        # self.button_prueba.pack()
        print("se han creado los widgets de pedidos")


    def destroy_widgets_orders(self):
        self.orders_frame.destroy()
        self.button_prueba.destroy()

    def go_to_order(self):
        pass