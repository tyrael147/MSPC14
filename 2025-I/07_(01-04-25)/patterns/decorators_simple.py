def my_simple_decorator(func):
    """A simple decorator that prints messages before and after function call."""
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper # Return the enhanced function

@my_simple_decorator
def say_hello():
    """A simple function that prints hello."""
    print("Hello!")

# Calling the decorated function
print("Calling say_hello:")
say_hello()

# Inspecting the function (notice its name is now 'wrapper')
print("\nInspecting the function name:")
print(say_hello.__name__)