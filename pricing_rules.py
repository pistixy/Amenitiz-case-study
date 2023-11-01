def apply_rules(cart):
    """
    Apply discount rules to the cart.
    
    Args:
    - cart (Cart): The shopping cart to which discount rules will be applied.
    """
    
    # Reset the current discount to ensure we're not stacking discounts from previous operations.
    cart.discount = 0

    # Rule: Buy-one-get-one-free for green tea
    if 'GR1' in cart.items:
        # Calculate the total price for all green teas in the cart
        total_greentea_price = cart.items['GR1']['product'].price * cart.items['GR1']['quantity']
        
        # Calculate the price after applying the buy-one-get-one-free discount
        # Every second green tea is free, so we divide the quantity by 2.
        # If there's an odd quantity, we add one more to account for the paid one.
        discounted_greentea_price = (cart.items['GR1']['quantity'] // 2 + cart.items['GR1']['quantity'] % 2) * cart.items['GR1']['product'].price
        
        # Update the discount amount for green tea
        cart.discount = (total_greentea_price - discounted_greentea_price)

    # Rule: Discounted price for strawberries for bulk purchases (3 or more)
    if 'SR1' in cart.items and cart.items['SR1']['quantity'] >= 3:
        # Calculate the total price for all strawberries in the cart
        total_strawberry_price = cart.items['SR1']['product'].price * cart.items['SR1']['quantity']
        
        # Calculate the price after applying the bulk discount
        discounted_strawberry_price = cart.items['SR1']['quantity'] * 4.5
        
        # Update the cumulative discount amount with the discount from strawberries
        cart.discount += (total_strawberry_price - discounted_strawberry_price)

    # Rule: 33% discount for 3 or more coffees
    if 'CF1' in cart.items and cart.items['CF1']['quantity'] >= 3:
        # Calculate the total price for all coffees in the cart
        total_coffee_price = cart.items['CF1']['product'].price * cart.items['CF1']['quantity']
        
        # Calculate the price after applying the 33% discount
        discounted_coffee_price = cart.items['CF1']['quantity'] * cart.items['CF1']['product'].price * 0.66
        
        # Update the cumulative discount amount with the discount from coffees
        cart.discount += (total_coffee_price - discounted_coffee_price)

    # NOTE: For adding new rules, continue the pattern above.
    # Calculate the total price for all items under the rule, calculate the discounted price,
    # and then update the cart's cumulative discount.
