

class   AllOrders():
    
    def __init__(self):
        self.list_unpaid_orders = []
        self.list_paid_orders = []

    def add_order(self, new_order):
        existing_order = 0
        for order in self.list_unpaid_orders:
            if order.client == new_order.client:
                existing_order = 1
                break
        if existing_order == 1:
            return (-1)
        else:
            self.list_unpaid_orders.append(new_order)
            return (0)
        
    def remove_order(self, order_to_remove):
        for i in range(len(self.list_unpaid_orders)):
            if self.list_unpaid_orders[i].client == order_to_remove.client:
                self.list_unpaid_orders.pop(i)
                return (0)
        return (-1)
        
