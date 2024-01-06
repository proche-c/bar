from clases.articulo import *

class Catalogue:
    
    def __init__(self):
        self.temp = []
        with open('articulos.txt', 'r') as self.fichero_items:
            for a in self.fichero_items:
                self.temp.append(a)
        self.list_items = []
        for a in self.temp:
            items = a.split(',')
            cat = items[2]
            p = Item(items[0], float(items[1]), cat[0:-1])
            self.list_items.append(p)

    def add_item(self, name, prize, category):
        new_item = Item(name, prize, category)
        self.list_items.append(new_item)
        fichero_items = open('articulos.txt', 'w')
        for a in self.list_items:
            fichero_items.write(a.name)
            fichero_items.write(",")
            fichero_items.write(str(a.prize))
            fichero_items.write(",")
            fichero_items.write(a.category)
            fichero_items.write("\n")
        fichero_items.close()

    def delete_item(self, name):
        for i in range(len(self.list_items)):
            if self.list_items[i].name == name:
                del self.list_items[i]
                break
        fichero_items = open('articulos.txt', 'w')
        for a in self.list_items:
            fichero_items.write(a.name)
            fichero_items.write(",")
            fichero_items.write(str(a.prize))
            fichero_items.write(",")
            fichero_items.write(a.category)
            fichero_items.write("\n")
        fichero_items.close()



# prueba = Catalogue()
# for item in prueba.list_items:
#     print(item.name + " " + str(item.prize) + " " + item.category)


# prueba.add_item("Cafe Cortado", 1, "Cafes")

# for item in prueba.list_items:
#     print(item.name + " " + str(item.prize) + " " + item.category)
# prueba.delete_item("Cubata normal")
# for item in prueba.list_items:
#     print(item.name + " " + str(item.prize) + " " + item.category)