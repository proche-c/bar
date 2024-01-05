import io
from clientes import *
from producto import *

# clientes = []
# clientes.append("Raul\n")
# clientes.append("Julia\n")
# clientes.append("Vasi y Ana\n")
# clientes.append("Ester y Luis\n")
# clientes.append("Nuri y Diego\n")
# fichero_clientes = open('clientes.txt', 'w')
# for cliente in clientes:
#     fichero_clientes.writelines(cliente)
# fichero_clientes.close()

# l_clientes = Clientes()
# l_clientes.add_cliente("Manola y Marina")
# print(l_clientes.lista_clientes)

articulo = []
p = ["Quinto o caña", "1.2", "Cervezas\n"]
articulo.append(p)
p = ["Tercio o copa", "1.5", "Cervezas\n"]
articulo.append(p)
p = ["Cubata normal", "4.5", "Bebidas\n"]
articulo.append(p)
fichero_articulos = open('articulos.txt', 'w')
for a in articulo:
    fichero_articulos.writelines(a)
fichero_articulos.close()