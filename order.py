from product import *

class   Order:
    def __init__(self, client):
        self.client = client
        self.products = []

    def add_product(self, product):
        self.products.add(product)

    def remove_product(self, name):
        for i in range(self.products):
            if self.products[i].name == name:
                self.products.remove(i)
                break