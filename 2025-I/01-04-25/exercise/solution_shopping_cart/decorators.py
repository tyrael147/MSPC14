"""
Decorators for the shopping cart system.
"""
from .constants import FIDELITY_POINTS

def membership_welcome(func):
    """
    Decorator that adds fidelity points and prints a welcome message for members.
    """
    def wrapper(*args, **kwargs):
        if kwargs['user'].get('membership', False):
            user_id = kwargs['user'].get('id')
            if user_id:
                # If the user does not exist, .get() will return 0 and we will add 1 to that.
                FIDELITY_POINTS[user_id] = FIDELITY_POINTS.get(user_id, 0) + 1
                print(f"Welcome back, thanks for being a member!")
        return func(*args, **kwargs)
    return wrapper 