"""
Shopping cart model with user support and error handling.
"""
from ..decorators import membership_welcome
from .product import create_product

class ShoppingCart:
    """Shopping cart with user support and error handling."""

    @membership_welcome
    def __init__(self, user:dict =None):
        self._items = {}  # Format: {product.name: {"product": product, "quantity": quantity, }}
        self.user = user

    def add_product(self, product_type: str, product_name:str, quantity=1):
        """Adds a product to the cart or increases its quantity."""
        try:
            product = create_product(product_type, product_name) # TODO

            if product.name in self._items:
                self._items[product.name]["quantity"] += quantity
            else:
                self._items[product.name] = {"product": product, "quantity": quantity}
        # except Exception as e:
            # print(f"We handle the error here")
        except:
            print("Error adding product")

    def remove_product(self, product_name:str, quantity:float=1):
        """Removes a product from the cart or reduces its quantity."""
        try:
            if product_name in self._items:
                if self._items[product_name]["quantity"] > quantity:
                    self._items[product_name]["quantity"] -= quantity
                else:
                    del self._items[product_name]
            else:
                print(f"Error: {product_name} is not in the cart.")
        except:
            print("Error removing product")

    def calculate_total(self)-> float:
        """Calculates the total cost of all items in the cart."""
        total = 0.0
        for item in self._items.values():
            total += item["product"].price * item["quantity"]
        return total

    def display_cart(self):
        """Displays all items in the cart with their details."""
        
        print("\nShopping Cart:")
        
        for name, item in self._items.items():
            product = item["product"]
            print(f"{item['quantity']} x {name} - ${product.price} each")
            
            # Display additional product information based on type
            if hasattr(product, 'get_expiration_date'):
                print(f"  Expires in: {product.get_expiration_date()} days")
           
            if hasattr(product, 'is_organic'):
                print(f"  Organic: {'Yes' if product.is_organic() else 'No'}")
                print(f"  Calories: {product.get_calories()}")
            
            if hasattr(product, 'is_safe_for_children'):
                print(f"  Safe for children: {'Yes' if product.is_safe_for_children() else 'No'}")
            
            if hasattr(product, 'get_sugar_content'):
                print(f"  Sugar content: {product.get_sugar_content()}g")
                print(f"  Container: {product.get_container_type()}")
        
        print(f"\nTotal: ${self.calculate_total()}") 