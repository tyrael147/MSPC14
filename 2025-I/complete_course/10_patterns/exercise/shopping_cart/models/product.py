"""
Product models for the shopping cart system.
"""
from ..constants import PRODUCT_TYPES

class Product:
    """Base class for all products."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - ${self.price:}")

class Food(Product):
    """Food products with additional attributes."""
    def __init__(self, name, price, expiration_days, organic, calories):
        super().__init__(name, price)
        ...
    def get_expiration_date(self):
        ...
    def is_organic(self):
        ...
    def get_calories(self):
        ...

class Cleaning(Product):
    """Cleaning products with safety information."""
    def __init__(self, name, price, safe_for_children):
        super().__init__(name, price)
        ...
    def is_safe_for_children(self):
        ...
class Drink(Product):
    """Drink products with container and sugar information."""
    def __init__(self, name, price, expiration_days, sugar_content, container):
        super().__init__(name, price)
        ...
    def get_expiration_date(self):
        ...
    def get_sugar_content(self):
        ...
    def get_container_type(self):
        ...

def create_product(product_type, name):
    """Factory function to create products based on type and name.
    This function MUST return a Product object.
    """

    product_data = PRODUCT_TYPES[product_type][name]
    
    if product_type == 'food':
        ...
    elif product_type == 'cleaning':
        ...
    elif product_type == 'drinks':
        ...