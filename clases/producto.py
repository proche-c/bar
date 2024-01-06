
class   Product:

    def __init__(self, name, prize, category): 
        self.name = name
        self.prize = prize
        self.category = category
        self.paid = 0

    def pay_product(self):
        self.paid = 1


