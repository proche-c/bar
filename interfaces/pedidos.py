from tkinter import *
from functools import partial

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
        self.F = []
        self.B = []
        for i in range(len(self.all_orders.list_unpaid_orders)):
            f = "f" + str(i)
            b = "b" + str(i)
            self.F.append(f)
            self.B.append(b)
        self.orders_frame = Frame(self, bg='#D7DEE0', height=300)
        self.orders_frame.pack(expand=True, fill='x')
        for i in range (len(self.F)):
            self.F[i] = Frame(self.orders_frame)
            self.F[i].pack(side='left', expand=True, fill='both')
            self.F[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
            self.B[i] = Button(self.F[i], text=self.all_orders.list_unpaid_orders[i].client, command=self.go_to_order)
            self.B[i].grid(row=0, column=0)
            self.F[i].grid_rowconfigure(0, weight=1)
            self.B[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
        self.frame_pedido = Frame(self, bg='#D7DEE0')
        self.frame_pedido.pack(expand=True, fill='both')
        self.frame_nuevo_pedido = Frame(self.frame_pedido)
        self.frame_nuevo_pedido.pack(expand=True, fill='both')
        self.frame_nuevo_pedido.config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
        self.button_nuevo_pedido = Button(self.frame_nuevo_pedido, text="NUEVO PEDIDO", command=self.go_to_order)
        self.button_nuevo_pedido.pack()
        self.button_nuevo_pedido.config(font=("Verdana", 16), bg='#D7DEE0', padx=12, pady=12)
        print("se han creado los widgets de pedidos")


    def destroy_widgets_orders(self):
        self.orders_frame.destroy()
        for i in range(len(self.F)):
            self.F[i].destroy()
            self.B[i].destroy()
        self.frame_pedido.destroy()
        self.frame_nuevo_pedido.destroy()
        self.button_nuevo_pedido.destroy()
        #self.button_prueba.destroy()

    def go_to_order(self):
        pass


    # def set_pedido_active(self, name, all_orders):
    #     pass
    
    # def create_widgets_orders(self):
    #     self.F1 = ["f1", "f2", "f3", "f4", "f5"]
    #     self.B1 = ["b1", "b2", "b3", "b4", "b5"]
    #     self.frame_ext_1 = Frame(self, bg='#D7DEE0', height=80)
    #     self.frame_ext_1.pack(expand=True, fill='x')
    #     #cad = 
    #     print("len of unpaid orders: " + str(len(self.all_orders.list_unpaid_orders)))
    #     for i in range (5):
    #         self.F1[i] = Frame(self.frame_ext_1)
    #         self.F1[i].pack(side='left', expand=True, fill='both')
    #         self.F1[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
    #         if len(self.all_orders.list_unpaid_orders) > i:
    #             to_write = self.all_orders.list_unpaid_orders[i].client
    #         else:
    #             to_write = ""
    #         self.B1[i] = Button(self.F1[i], text=to_write, command=self.set_pedido_active)
    #         self.B1[i].grid(row=0, column=0)
    #         self.F1[i].grid_rowconfigure(0, weight=1)
    #         self.B1[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
    #     self.F2 = ["f6", "f7", "f8", "f9", "f10"]
    #     self.B2 = ["b6", "b7", "b8", "b9", "b10"]
    #     self.frame_ext_2 = Frame(self, bg='#D7DEE0', height=80)
    #     self.frame_ext_2.pack(expand=True, fill='x')
    #     for i in range (5):
    #         self.F2[i] = Frame(self.frame_ext_2)
    #         self.F2[i].pack(side='left', expand=True, fill='both')
    #         self.F2[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
    #         if len(self.all_orders.list_unpaid_orders) > i + 5:
    #             to_write = self.all_orders.list_unpaid_orders[i + 5].client
    #         else:
    #             to_write = ""
    #         self.B1[i] = Button(self.F2[i], text=to_write, command=self.set_pedido_active)
    #         self.B2[i].grid(row=0, column=0)
    #         self.F2[i].grid_rowconfigure(0, weight=1)
    #         self.B2[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
    #     self.F3 = ["f11", "f12", "f13", "f14", "f15"]
    #     self.B3 = ["b11", "b12", "b13", "b14", "b15"]
    #     self.frame_ext_3 = Frame(self, bg='#D7DEE0', height=80)
    #     self.frame_ext_3.pack(expand=True, fill='x')
    #     for i in range (5):
    #         self.F3[i] = Frame(self.frame_ext_3)
    #         self.F3[i].pack(side='left', expand=True, fill='both')
    #         self.F3[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
    #         self.B3[i] = Button(self.F3[i], text=self.all_orders.list_unpaid_orders[i + 10].client, command=self.set_pedido_active)
    #         self.B3[i].grid(row=0, column=0)
    #         self.F3[i].grid_rowconfigure(0, weight=1)
    #         self.B3[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
    #     self.F4 = ["f16", "f17", "f18", "f19", "f20"]
    #     self.B4 = ["b16", "b17", "b18", "b19", "b20"]
    #     self.frame_ext_4 = Frame(self, bg='#D7DEE0', height=80)
    #     self.frame_ext_4.pack(expand=True, fill='x')
    #     for i in range (5):
    #         self.F4[i] = Frame(self.frame_ext_4)
    #         self.F4[i].pack(side='left', expand=True, fill='both')
    #         self.F4[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
    #         self.B4[i] = Button(self.F4[i], text=self.all_orders.list_unpaid_orders[i + 15].client, command=self.set_pedido_active)
    #         self.B4[i].grid(row=0, column=0)
    #         self.F4[i].grid_rowconfigure(0, weight=1)
    #         self.B4[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
    #     self.F5 = ["f21", "f22", "f23", "f24", "f25"]
    #     self.B5 = ["b21", "b22", "b23", "b24", "b25"]
    #     self.frame_ext_5 = Frame(self, bg='#D7DEE0', height=80)
    #     self.frame_ext_5.pack(expand=True, fill='x')
    #     for i in range (5):
    #         self.F5[i] = Frame(self.frame_ext_5)
    #         self.F5[i].pack(side='left', expand=True, fill='both')
    #         self.F5[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
    #         self.B5[i] = Button(self.F5[i], text=self.all_orders.list_unpaid_orders[i + 20].client, command=self.set_pedido_active)
    #         self.B5[i].grid(row=0, column=0)
    #         self.F5[i].grid_rowconfigure(0, weight=1)
    #         self.B5[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
    #     self.F6 = ["f26", "f27", "f28", "f29", "f30"]
    #     self.B6 = ["b26", "b27", "b28", "b29", "b30"]
    #     self.frame_ext_6 = Frame(self, bg='#D7DEE0', height=80)
    #     self.frame_ext_6.pack(expand=True, fill='x')
    #     for i in range (5):
    #         self.F6[i] = Frame(self.frame_ext_6)
    #         self.F6[i].pack(side='left', expand=True, fill='both')
    #         self.F6[i].config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
    #         self.B6[i] = Button(self.F6[i], text=self.all_orders.list_unpaid_orders[i + 25].client, command=self.set_pedido_active)
    #         self.B6[i].grid(row=0, column=0)
    #         self.F6[i].grid_rowconfigure(0, weight=1)
    #         self.B6[i].config(font=("Verdana", 14), bg='#D7DEE0', padx=2, pady=2)
    #     self.frame_pedido = Frame(self, bg='#D7DEE0')
    #     self.frame_pedido.pack(expand=True, fill='both')
    #     self.frame_nuevo_pedido = Frame(self.frame_pedido)
    #     self.frame_nuevo_pedido.pack(expand=True, fill='both')
    #     self.frame_nuevo_pedido.config(bg='#D7DEE0', bd=5, relief='ridge', padx=10, pady=6)
    #     self.button_nuevo_pedido = Button(self.frame_nuevo_pedido, text="NUEVO PEDIDO", command=self.set_pedido_active)
    #     self.button_nuevo_pedido.pack()
    #     self.button_nuevo_pedido.config(font=("Verdana", 16), bg='#D7DEE0', padx=12, pady=12)

    # def destroy_widgets_tables(self):
    #     for i in range(5):
    #         self.B1[i].destroy()
    #         self.F1[i].destroy()
    #         self.B2[i].destroy()
    #         self.F2[i].destroy()
    #         self.B3[i].destroy()
    #         self.F3[i].destroy()
    #         self.B4[i].destroy()
    #         self.F4[i].destroy()
    #         self.B5[i].destroy()
    #         self.F5[i].destroy()
    #         self.B6[i].destroy()
    #         self.F6[i].destroy()
    #     self.frame_ext_1.destroy()
    #     self.frame_ext_2.destroy()
    #     self.frame_ext_3.destroy()
    #     self.frame_ext_4.destroy()
    #     self.frame_ext_5.destroy()
    #     self.frame_ext_6.destroy()