### Decorator with args and kwargs

def decorator_accepting_args(func):
    """A decorator for functions that accept arguments."""
    def wrapper(*args, **kwargs):
        print(f"Wrapper: Calling function '{func.__name__}' with arguments:")
        print(f"  Positional args: {args}")
        print(f"  Keyword args: {kwargs}")
        # Call the original function, passing arguments through
        result = func(*args, **kwargs)
        print(f"Wrapper: Function '{func.__name__}' finished execution.")
        return result # Return the result of the original function
    return wrapper

@decorator_accepting_args
def greet(name, greeting="Hello"):
    """Greets a person with a specific greeting."""
    print(f"{greeting}, {name}!")
    return f"Greeting for {name} complete."

# Calling the decorated function with arguments
print("Calling greet:")
return_value = greet("Alice", greeting="Hi")
print(f"Returned value: {return_value}")

print("\nCalling greet with only positional argument:")
greet("Bob")

# Inspecting the function name
print("\nInspecting the function name:")
print(greet.__name__)