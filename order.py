from product import *

class   Order:
    def __init__(self, client):
        self.client = client
        self.products = []
        self.total = 0
        self.paid = 0
        self.remaining = 0

    def add_product(self, product):
        self.products.add(product)

    def remove_product(self, name):
        for i in range(self.products):
            if self.products[i].name == name:
                self.products.remove(i)
                break

    def pay(self, products_to_pay):
        for p in products_to_pay:
            self.paid = self.paid + p.prize