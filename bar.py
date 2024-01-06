from tkinter import *
from interfaces.header import *
from interfaces.body import *
from interfaces.footer import *
from clases.catalogo import *
from clases.clientes import *

all_orders = []
clients = Clients()
#print(clients.list_clients)
catalogue = Catalogue()

root = Tk()
y = round((root.winfo_screenheight() - 1000) / 2)
x = round((root.winfo_screenwidth() - 600) / 2)
w = 1000
h = 600
root.geometry(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
root.resizable(0,0)
root.configure(bg='#525252')
root.title("")
header = Header(root)
body = Body(all_orders, clients, catalogue, root)
footer = Footer(root)
root.mainloop()
