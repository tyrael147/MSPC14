"""
Product models for the shopping cart system.
"""
from ..constants import PRODUCT_TYPES
from abc import ABC

class Product(ABC):
    """Base class for all products."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - ${self.price:.2f}")

class Food(Product):
    """Food products with additional attributes."""
    def __init__(self, name, price, expiration_days, organic, calories):
        super().__init__(name, price)
        self.expiration_days = expiration_days
        self.organic = organic
        self.calories = calories

    def get_expiration_date(self):
        """Returns the expiration date based on days from now."""
        return self.expiration_days

    def is_organic(self):
        """Returns whether the food is organic."""
        return self.organic

    def get_calories(self):
        """Returns the calorie content."""
        return self.calories

class Cleaning(Product):
    """Cleaning products with safety information."""
    def __init__(self, name, price, safe_for_children):
        super().__init__(name, price)
        self.safe_for_children = safe_for_children

    def is_safe_for_children(self):
        """Returns whether the product is safe for children."""
        return self.safe_for_children

class Drink(Product):
    """Drink products with container and sugar information."""
    def __init__(self, name, price, expiration_days, sugar_content, container):
        super().__init__(name, price)
        self.expiration_days = expiration_days
        self.sugar_content = sugar_content
        self.container = container

    def get_expiration_date(self):
        """Returns the expiration date based on days from now."""
        return self.expiration_days

    def get_sugar_content(self):
        """Returns the sugar content in grams."""
        return self.sugar_content

    def get_container_type(self):
        """Returns the container type."""
        return self.container

def create_product(product_type:str, name:str):
    """Factory function to create products based on type and name."""
    product_data = PRODUCT_TYPES[product_type][name]
    
    if product_type == 'food':
        return Food(
            name=name,
            price=product_data['price'],
            expiration_days=product_data['expiration_days'],
            organic=product_data['organic'],
            calories=product_data['calories']
        )
    elif product_type == 'cleaning':
        return Cleaning(
            name=name,
            price=product_data['price'],
            safe_for_children=product_data['safe_for_children']
        )
    elif product_type == 'drinks':
        return Drink(
            name=name,
            price=product_data['price'],
            expiration_days=product_data['expiration_days'],
            sugar_content=product_data['sugar_content'],
            container=product_data['container']
            )