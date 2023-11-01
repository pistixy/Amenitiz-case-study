class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        total_price = sum(item.price for item in self.items)
        return total_price
    
    def display(self):
        print("Items in cart: ")
        for item in self.items:
            print(item.name, item.price)
        print("Total price:", self.total())