### Decorator that takes arguments

def repeat(num_times):
    """Decorator factory: Creates a decorator that repeats a function call."""
    def decorator_repeat(func):
        """The actual decorator returned by the factory."""
        def wrapper(*args, **kwargs):
            """The final wrapper executing the logic."""
            print(f"Wrapper: Will repeat function '{func.__name__}' {num_times} times.")
            last_result = None
            for i in range(num_times):
                print(f"  Repetition {i+1}/{num_times}")
                last_result = func(*args, **kwargs)
            print(f"Wrapper: Finished repeating.")
            return last_result # Return the result of the last call
        return wrapper
    return decorator_repeat # Return the decorator

@repeat(num_times=3)
def say_whee(name):
    """Prints Whee! with a name."""
    print(f"Whee, {name}!")
    return f"Whee for {name} done."

# Calling the decorated function
print("Calling say_whee:")
result = say_whee("Charlie")
print(f"Final returned value: {result}")

# Inspecting the function name
print("\nInspecting the function name:")
print(say_whee.__name__)