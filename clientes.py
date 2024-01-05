import pickle

class Clientes:

    def __init__(self):
        self.lista_clientes = []
        self.fichero_clientes = open('clientes.txt', 'r')
        self.lista_clientes = self.fichero_clientes.readlines()
        self.fichero_clientes.close()
        print(self.lista_clientes)

    def add_cliente(self, name):
        cad = name + '\n'
        self.lista_clientes.append(cad)
        self.fichero_clientes = open('clientes', 'w')
        for cliente in self.lista_clientes:
            self.fichero_clientes.writelines(cliente)
        self.fichero_clientes.close()
