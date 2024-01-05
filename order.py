from producto import *

class   Order:
    def __init__(self, client):
        self.client = client
        self.products = []
        self.total = 0
        self.paid = 0
        self.remaining = 0

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for i in range(self.products):
            if self.products[i].name == name:
                self.products.remove(i)
                break

    def pay_total(self):
        for p in self.products:
            self.paid = self.paid + p.prize

    def pay_product(self, product_to_pay):
        product_to_pay.paid = 1
        self.paid = self.paid + product_to_pay.prize