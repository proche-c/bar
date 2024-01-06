
from order import *

class AllOrders:
    
    def __init__(self):
        self.list_orders = []

    def add_order(self, order):
        self.list_orders.append(order)