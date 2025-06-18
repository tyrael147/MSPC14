class Order:
    """Manages a single customer order, tracking items and calculating totals."""

    def __init__(self, order_id:str):
        """
        Initializes a new order with a unique ID and an empty list of items.

        Args:
            order_id (str or int): A unique identifier for the order.
        """
        self.order_id = order_id
        self.items = []
        print(f"Order {self.order_id} started.")

    def add_item(self, item):
        """
        Adds an item (like a Burger object) to the order.
        """
        # Assume item object has get_name() and get_price() methods
        try:
            burger_name = item.get_name()
            burger_price = item.get_price()
        except:
            print("Error: Provided item does not have get_name() or get_price() method.")
            return

        if burger_price <= 0:
            print("Item price must be positive.")
            return

        self.items.append({'name': burger_name, 'price': burger_price})
        print(f'"{burger_name}" added to order.')

    def get_total(self):
        """Calculates the total cost of all items in the order."""
        total = 0
        for item in self.items:
            total += item['price']
        return total

    def details(self):
        """
        Generates a multi-line string representing the order receipt.

        Returns:
            str: A formatted string showing order ID, items, and total.
        """
        print(f"\nOrder ID: {self.order_id}\n")

        if not self.items:
            print("\n(No items in this order)")
        else:
            for item in self.items:
                print(f"- {item['name']}: ${item['price']}")

        total = self.get_total()
        print(f"\nTotal: ${total}\n")
