from clases.producto import *
import datetime

class   Order:
    def __init__(self, client):
        self.client = client
        self.unpaid_products = []
        self.paid_products = []
        self.date_order = datetime.datetime.now()
        self.total = 0
        self.paid = 0
        self.remaining = 0

    def add_product(self, product):
        self.unpaid_products.append(product)

    def remove_product(self, name):
        for i in range(len(self.unpaid_products)):
            if self.unpaid_products[i].name == name:
                self.unpaid_products.remove(i)
                break

    def pay_total(self):
        for i in range(len(self.unpaid_products)):
            self.paid = self.paid + self.unpaid_products[i].prize
            self.paid_products.append(i)
            self.unpaid_products.pop(i)

    def pay_products(self, products_to_pay):
        for i in range(len(products_to_pay)):
            products_to_pay[i].paid = 1
            self.paid = self.paid + products_to_pay[i].prize
            self.paid_products.append(i)
            self.unpaid_products.pop(i)
