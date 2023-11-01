# Amenitiz-case-study

The case study for the interview process at Amenitiz by István Takó

## Shopping Cart System

This project provides a simple shopping cart system with a few products and associated discount rules. The user can enter a list of product codes, and the system will calculate the total price with and without discounts.

## Features

- Modular and object-oriented design.
- Ability to add products to a cart.
- Dynamic application of pricing rules.
- Display cart contents with individual product details and total prices.

## Directory Structure


|- main.py                 # Main entry point of the application.
|- cart.py                 # Defines the Cart class for managing shopping cart operations.
|- product.py              # Defines the Product class for product-related operations.
|- products.py             # Contains the available products in the store.
|- pricing_rules.py        # Contains various discount rules for products.
|- README.md               # This file.

## How to Run

1. Ensure you have Python 3 installed.
2. Clone or download the repository to your local machine.
3. Navigate to the project directory in the terminal or command prompt.
4. Run `python main.py`.
5. Follow the prompts to enter product codes separated by commas.

## Products

The following products are available:

- Green Tea (Code: GR1)
- Strawberries (Code: SR1)
- Coffee (Code: CF1)

## Pricing Rules

- Green Tea: Buy one get one free.
- Strawberries: Bulk purchases (3 or more) at €4.5 each.
- Coffee: 33% discount for 3 or more.

## Future Improvements

- Implementing more discount rules as separate classes for extensibility.
- Adding error handling for better user experience.
- Enhancing the interface for user interactions.
