import io
import os

class Clients:

    def __init__(self):
        temp = []
        self.list_clients = []
        file_temp = open('clientes.txt', 'a')
        if os.path.getsize('clientes.txt') > 0:
            file_temp.close()
            with open('clientes.txt', 'r') as fichero_clients:
                for c_temp in fichero_clients:
                    temp.append(c_temp)
            for c_temp in temp:
                c = c_temp[0:-1]
                self.list_clients.append(c)
        else:
            file_temp.close()

    def add_client(self, name):
        self.list_clients.append(name)
        fichero_clients = open('clientes.txt', 'w')
        for client in self.list_clients:
            fichero_clients.write(client)
            fichero_clients.write("\n")
        fichero_clients.close()

    def delete_client(self, name):
        for i in range(len(self.list_clients)):
            if self.list_clients[i] == name:
                del self.list_clients[i]
                break
        fichero_clients = open('clientes.txt', 'w')
        for c in self.list_clients:
            fichero_clients.write(c)
            fichero_clients.write("\n")
        fichero_clients.close()

# list_cl = Clients()
# # for c in list_cl.list_clients:
# #     print(c)

# list_cl.add_client("Miguel y Josefina")
# list_cl.add_client("Oscar y Ana")
# list_cl.add_client("Ruben y Zulema")
# for c in list_cl.list_clients:
#     print(c)

