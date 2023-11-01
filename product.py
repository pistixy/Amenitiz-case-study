class Product:
    """
    Represents a product with a code, name, and price.
    """

    def __init__(self, code, name, price):
        """
        Initializes a new Product instance.

        Args:
        - code (str): The unique identifier for the product.
        - name (str): The human-readable name of the product.
        - price (float): The price of the product.
        """
        self.code = code  # Unique product code (e.g., 'GR1')
        self.name = name  # Human-readable product name (e.g., 'Green Tea')
        self.price = price  # Price of the product in currency units (e.g., 3.11€)
