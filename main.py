from cart import Cart
from product import Product



green_tea = Product('GR1', 'Green Tea', 3.11)
strawberry = Product('SR1', 'Strawberries', 5.00)
coffee = Product('CF1', 'Coffee', 11.23)

cart = Cart()
cart.add(green_tea)
cart.add(strawberry)
cart.add(coffee)

cart.display()

