from .constants import CONSTANTS

class Burger:
    """Represents a single burger item with customizable toppings."""

    def __init__(self): # This is complete
        """Initializes a basic burger with no patty or cheese added yet."""
        self.patty = False
        self.cheese = False
        self.base_price = CONSTANTS['BURGUER_BASE_PRICE']

    def add_patty(self): # THis is missing
        """Adds a patty to the burger."""
        ...

    def add_cheese(self): # This is missing
        """Adds cheese to the burger."""
        ...

    def get_price(self) -> float : # This is missing
        """Calculates the total price of the burger based on added toppings."""
        ...

    def get_name(self)-> str:
        """Generates the display name for the burger based on added toppings."""
        ...
