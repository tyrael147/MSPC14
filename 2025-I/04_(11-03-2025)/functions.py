# %% [markdown]
# # Functions
#
# The concept of functions in python are analogous to the concept of functions in math. 
#
#  $$ z = f(x,y)$$

# %% [markdown]
# In python, functions are more versatile and generic than mathematic functions. In fact, they contain reusable blocks of code that can perform a specific task. 
# They help in organizing code, reducing redundancy, and improving modularity.

# %% [markdown]
# Basic Syntax
# ```python
# def function_name(<your-parameters>):
#     <your code block here>
#     return <and output value>      # Optional return statement
# ```
# - **`def`**: Keyword to define a function
# - **\<your-parameters\>**: Inputs to the function (optional)
# - **`return`**: Returns a value (optional; defaults to `None`)

# %%
# A basic function needs to use indentation to indicate scope
def greet():
    print("Hello, World!")

greet()  # Function call

# %% [markdown]
# About arguments and parameters:
#
# - **Required Parameters**: Must be passed during the function call
# - **Default Parameters**: Have default values if not provided
# - **Keyword Arguments**: Specified by parameter name
# - **Variable-length Arguments**: `*args` (tuples) and `**kwargs` (dictionaries)

# %%
# Example 2: Function with Parameters
def add(a, b):
    """Returns the sum of two numbers""" # Docstrings can be used to give more information about the function
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# %%
# We can create default parameters when using the = operator
def power(base, exponent=2):
    """Returns base raised to the exponent (default: squared)"""
    return base ** exponent

print(power(3))      # Uses default exponent (2)
print(power(2, 4))   # Overrides default exponent

# %%
# Arguments are passed to each corresponding parameter using the assign operator
def person_info(name, age, city):
    print(f"{name}, {age} years old, lives in {city}")

person_info(age=30, city="Paris", name="Alice")  # Order doesn't matter

# %% [markdown]
# In python we can ingest arguments in a flexible manner using `*args` and `**kwargs`.
#

# %%
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 'a', name="John", age=25)

# %% [markdown]
# A function can return one or more values when `return` is defined, otherwise it return `None`

# %%
# call the print_args() function with the arguments of your choice and assign the output to a variable named 'a'

# %%
# If needed, we can return multiple outputs, but may need to unpack them when assigning them to variables

def calculate(a, b):
    return a + b, a - b, a * b

sum_result, diff_result, product_result = calculate(10, 5)
print(f"Sum: {sum_result}, Difference: {diff_result}, Product: {product_result}")

# %% [markdown]
# The indentation is important because it defines the scope of the function.
# - **Local Variables**: Defined inside a function (not accessible outside)
# - **Global Variables**: Defined outside a function (accessible but not modifiable without `global` keyword)

# %%

global_var = "I'm global"

def test_scope():
    local_var = "I'm local"
    print(global_var)        # Accessible
    print(local_var)         # Accessible

test_scope()
# print(local_var) 
