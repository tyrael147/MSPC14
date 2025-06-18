from .products import Burger

class Order:
    """Manages a single customer order, tracking items and calculating totals."""

    def __init__(self, order_id): # This is complete
        """
        Initializes a new order with a unique ID and an empty list of items.
        """
        self.order_id = order_id
        self.items = []
        print(f"Order {self.order_id} started.")

    def add_item(self, burger: Burger): # This is missing
        """
        Adds an item (like a Burger object) to the order.
        """
        # Complete here
        ...

    def get_total(self)-> float: # This is missing
        """Calculates the total cost of all items in the order."""
        # Complete here
        ...

    def details(self): # This is complete
        """
        Generates a multi-line string representing the order receipt.
        """

        print(f"\nOrder ID: {self.order_id}\n")

        if not self.items:
            print("\n(No items in this order)")
        else:
            for item in self.items:
                print(f"- {item['name']}: ${item['price']}")

        total = self.get_total()
        print(f"\nTotal: ${total}\n")
