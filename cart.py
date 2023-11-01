from pricing_rules import apply_rules

class Cart:
    def __init__(self):
        # Initializes an empty dictionary to store items. 
        # Each key represents a product code and the corresponding value is another dictionary 
        # containing the product object and its quantity.
        self.items = {}

    def add(self, product):
        """Adds a product to the cart or increases its quantity if already present."""

        # Check if the product is already in the cart
        if product.code in self.items:
            # If yes, just increase its quantity by 1
            self.items[product.code]['quantity'] += 1
        else:
            # Otherwise, add the product to the cart with a quantity of 1
            self.items[product.code] = {'product': product, 'quantity': 1}

    def total(self):
        """Returns the total price of items in the cart without discounts."""

        # Calculate the sum of the price of each product multiplied by its quantity
        return sum(item['product'].price * item['quantity'] for item in self.items.values())
    
    def apply_rules(self):
        """Applies pricing rules to the cart to calculate discounts."""

        # The actual discount logic is imported from the pricing_rules module
        self.discount = apply_rules(self)
    
    def total_with_discounts(self):
        """Returns the total price of items in the cart after applying discounts."""

        # Calculate the initial total price without discounts
        total_price = sum(item['product'].price * item['quantity'] for item in self.items.values())
        # Apply the pricing rules to get the discounts
        self.apply_rules()
        # Subtract the discount from the initial total to get the final total
        return total_price - self.discount

    def display(self):
        """Displays the content of the cart, including product details, quantities, and prices."""

        # Header
        header_format = "{:<10} | {:<20} | {:<10} | {:<10} | {:<15}"
        separator = "-" * 75  # Visual separator line

        print("\nItems in cart:")
        print(separator)
        print(header_format.format("CODE", "PRODUCTNAME", "PRICE ", "QUANTITY", "TOTAL PRICE"))
        print(separator)

        # Print details for each item in the cart
        item_format = "{:<10} | {:<20} | {:<10.2f}€ | {:<10} | {:<15.2f}€"
        for item_code, item_details in self.items.items():
            product = item_details['product']
            quantity = item_details['quantity']
            total_price_for_item = product.price * quantity
            print(item_format.format(product.code, product.name, product.price, quantity, total_price_for_item))
        
        print(separator)
        # Print the overall total and the total with discounts applied
        print("\nOverall Total price:", "{:.2f}€".format(self.total()))
        print("Total after discounts:", "{:.2f}€".format(self.total_with_discounts()))
        print(separator)

