from cart import Cart
from product import Product
from products import products

def main():
    # Instantiate a new Cart object
    cart = Cart()

    # Prompt the user to enter product codes separated by commas
    input_codes = input("Enter product codes separated by commas (e.g., GR1,SR1,CF1): ").strip().upper()
    
    # Process the user input: split by commas and strip any extra spaces
    codes = [code.strip() for code in input_codes.split(",")]

    # Add the corresponding products to the cart based on the provided codes
    for code in codes:
        # Check if the provided product code exists in the available products
        if code in products:
            cart.add(products[code])
        else:
            # Notify the user if a provided product code is not recognized
            print(f"Product code {code} not recognized.")

    # Display the content of the cart, including product details and prices
    cart.display()

# Ensures the main function is executed only when this script is run directly and not imported
if __name__ == "__main__":
    main()
