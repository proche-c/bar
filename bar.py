from tkinter import *
from interfaces.header import *
from interfaces.body import *
from interfaces.footer import *
from clases.catalogo import *
from clases.clientes import *
from clases.all_orders import *

# creo una instancia de all_orders, que serán todas los pedidos activos
# creo una instancia de Clients, que es la lista de clientes que toma los datos del archivo 'clientes.txt'
# creo una instancia de Catalogue, que es la lista de los productos y toma los datos del archivo 'articulos.txt'
all_orders = AllOrders()
clients = Clients()
catalogue = Catalogue()


# Se abre la interfaz gráfica
root = Tk()
y = round((root.winfo_screenheight() - 1000) / 2)
x = round((root.winfo_screenwidth() - 520) / 2)
w = 1000
h = 520
root.geometry(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
root.resizable(0,0)
root.configure(bg='#525252')
root.title("")
header = Header(root)
body = Body(all_orders, clients, catalogue, root)
footer = Footer(root)
root.mainloop()


# en el header falta que se vaya actualizando la hora, NO ES IMPORTANTE