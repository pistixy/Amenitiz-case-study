from product import Product

# Dictionary containing the available products.
# Key: Product code (e.g., 'GR1')
# Value: Product object containing details like product name and price.
products = {
    'GR1': Product('GR1', 'Green Tea', 3.11),      
    'SR1': Product('SR1', 'Strawberries', 5.00),  
    'CF1': Product('CF1', 'Coffee', 11.23)         
}
