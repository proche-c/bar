
class   Item:

    def __init__(self, name, prize, category): 
        self.name = name
        self.prize = prize
        self.category = category

    def pay_product(self):
        self.paid = 1

