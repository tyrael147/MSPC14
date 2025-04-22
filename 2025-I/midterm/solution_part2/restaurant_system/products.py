from .constants import CONSTANTS

class Burger:
    """Represents a single burger item with customizable toppings."""

    def __init__(self):
        """Initializes a basic burger with no patty or cheese added yet."""
        self.patty = False
        self.cheese = False
        self.base_price = CONSTANTS['BURGUER_BASE_PRICE']

    def add_patty(self):
        """Adds a patty to the burger."""
        self.patty = True
        print("Patty added...")

    def add_cheese(self):
        """Adds cheese to the burger."""
        self.cheese = True
        print("Cheese added...")

    def get_price(self):
        """Calculates the total price of the burger based on added toppings."""
        total_price = self.base_price
        if self.patty:
            total_price += CONSTANTS['ADDITIONAL_PATTY_PRICE']
        if self.cheese:
            total_price += CONSTANTS['ADDITIONAL_CHEESE_PRICE']
        return total_price

    def get_name(self):
        """Generates the display name for the burger based on added toppings."""
        if self.cheese and self.patty:
            return "Cheese Burger"
        if self.cheese and not self.patty:
            return "Veggie Cheese Burger"
        elif self.patty:
                return "Burger"
