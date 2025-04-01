"""
Example usage of the shopping cart system.
"""
import shopping_cart
from shopping_cart.models.cart import ShoppingCart
from shopping_cart import constants


def test_cart():


    # Create a user with membership
    user = {
        'id': 'user123',
        'name': 'John Doe',
        'membership': True
    }
    
    # Create a shopping cart for the user
    cart = ShoppingCart(user=user)
    
    # Add some food items
    # cart.add_product('food', 'milk', 2)
    cart.add_product('food', 'bread', 1)
    cart.add_product('food', 'bananas', 3)
    
    # Add cleaning products
    cart.add_product('cleaning', 'dish_soap', 1)
    
    # Add drinks
    cart.add_product('drinks', 'orange_juice', 2)
    
    # Display the cart
    cart.display_cart()
    
    # Remove some items
    cart.remove_product('milk', 1)
    cart.remove_product('bananas')
    
    # Display the updated cart
    cart.display_cart()

    print("Fidelity points: ", constants.FIDELITY_POINTS)
    print("Version: ", shopping_cart.__version__)
if __name__ == '__main__':
    test_cart() 