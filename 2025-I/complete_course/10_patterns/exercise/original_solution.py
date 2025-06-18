# # Solution: Shopping system

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - ${self.price}")


class ShoppingCart:
    def __init__(self):
        self._items = {}  # Format: {product.name: {"product": product, "quantity": quantity}}

    def add_product(self, product, quantity=1):
        if product.name in self._items:
            self._items[product.name]["quantity"] += quantity
        else:
            self._items[product.name] = {"product": product, "quantity": quantity}

    def remove_product(self, product, quantity=1):
        if product.name in self._items:
            if self._items[product.name]["quantity"] > quantity:
                self._items[product.name]["quantity"] -= quantity
            else:
                del self._items[product.name]
        else:
            print(f"Error: {product.name} is not in the cart.")

    def calculate_total(self):
        total = 0.0
        for item in self._items.values():
            total += item["product"].price * item["quantity"]
        return total

    def display_cart(self):
        print("Shopping Cart:")
        for name, item in self._items.items():
            print(f"{item['quantity']} x {name} - {item['product'].price} each")
        print(f"Total: {self.calculate_total()}\n")


# Test the implementation
# Create products
apple = Product("Apple", 0.99)
banana = Product("Banana", 0.59)
milk = Product("Milk", 3.49)

# Create cart
cart = ShoppingCart()

# Add items
cart.add_product(apple, 3)
cart.add_product(banana)
cart.add_product(milk, 2)
cart.display_cart()

# Remove items
cart.remove_product(apple, 1)
cart.remove_product(banana)
cart.display_cart()

# Try to remove a product not in the cart
cart.remove_product(milk, 5)  # Removes all milk
cart.display_cart()