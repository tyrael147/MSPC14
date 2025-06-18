"""
Constants for the shopping cart system.
"""

PRODUCT_TYPES = {
    'food': {
        'milk': {'price': 3.49, 'expiration_days': 7, 'organic': True, 'calories': 103},
        'bread': {'price': 2.99, 'expiration_days': 5, 'organic': False, 'calories': 265},
        'eggs': {'price': 4.99, 'expiration_days': 14, 'organic': True, 'calories': 155},
        'bananas': {'price': 0.59, 'expiration_days': 7, 'organic': True, 'calories': 105},
        'chicken_breast': {'price': 6.99, 'expiration_days': 3, 'organic': False, 'calories': 165}
    },
    'cleaning': {
        'dish_soap': {'price': 2.99, 'safe_for_children': True},
        'laundry_detergent': {'price': 12.99, 'safe_for_children': False}
    },
    'drinks': {
        'bottled_water': {'price': 1.99, 'expiration_days': 365, 'sugar_content': 0, 'container': 'plastic'},
        'soda': {'price': 2.99, 'expiration_days': 180, 'sugar_content': 39, 'container': 'tin can'},
        'orange_juice': {'price': 3.99, 'expiration_days': 7, 'sugar_content': 22, 'container': 'glass bottle'}
    }
}

FIDELITY_POINTS = {} 