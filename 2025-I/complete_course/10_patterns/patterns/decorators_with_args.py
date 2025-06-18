### Decorator with arguments
def decorator_accepting_args(func):
    """A decorator for functions that accept arguments."""
    def wrapper(first, second):
        print(f"Wrapper: Calling function '{func.__name__}' with arguments:")
        first = first * 2
        second = second * 3
        # Call the original function, passing arguments through
        result = func(first, second)
        print(f"Wrapper: Function '{func.__name__}' finished execution.")
        return result # Return the result of the original function
    return wrapper

@decorator_accepting_args
def basic_function(first_number, second_number):
    print("first_number", first_number)
    print("second_number", second_number)

basic_function(2, 3)
