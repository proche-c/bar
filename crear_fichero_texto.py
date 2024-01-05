import io
from clientes import *

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

l_clientes = Clientes()
l_clientes.add_cliente("Manola y Marina")
print(l_clientes.lista_clientes)