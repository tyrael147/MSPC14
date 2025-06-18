# %% [markdown]
# # If Statements
# The `if` statement executes code blocks based on boolean conditions.
#
# **Syntax:**
# ```python
# if condition:
#     # indented code block
# ```
#
# **Key Rules:**
# - Mandatory colon `:` after the condition
# - Code blocks defined by indentation (4 spaces recommended)
# - Comparison operators: `>`, `<`, `==`, `!=`, `>=`, `<=`

# %%
temperature = 30
if temperature > 25:
    print("It's a hot day!")
    print("Stay hydrated!")

# %% [markdown]
# ## If-Else Statement
# Provides alternative execution paths:
# ```python
# if condition:
#     # true case
# else:
#     # false case
# ```

# %%
age = 17
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote yet")
    years_left = 18 - age
    print(f"Come back in {years_left} year{'s' if years_left > 1 else ''}")

# %% [markdown]
# ## Elif (Else If) Statements
# Handles multiple exclusive conditions:
# ```python
# if cond1:
#     ...
# elif cond2:
#     ...
# else:
#     ...
# ```

# %%
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score} -> Grade: {grade}")

# %% [markdown]
# ## Truthiness and Boolean Evaluation
# Python evaluates non-boolean values in conditions:
# - **Falsy:** `None`, `0`, empty collections (`""`, `[]`, `{}`, etc.)
# - **Truthy:** All other values

# %%
username = ""
if username:
    print(f"Welcome {username}")
else:
    print("Guest user")

# %% [markdown]
# ## Logical Operators
# Combine conditions with:
# - `and`: Both must be true
# - `or`: At least one true
# - `not`: Inverts boolean

# %%
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive a car")
else:
    print("Driving not allowed")

# %% [markdown]
# ## Nested If Statements
# If statements can contain other if statements

# %%
account_balance = 1500
is_premium = True
if account_balance > 0:
    print("Account active")
    if is_premium:
        print("Premium benefits activated")
    else:
        print("Standard account")
else:
    print("Account suspended")

# %% [markdown]
# ## Ternary Operator
# Compact conditional expression:
# ```python
# result = true_value if condition else false_value
# ```

# %%
temperature = 28
status = "Hot" if temperature > 25 else "Cool"
print(f"Status: {status}")

# %% [markdown]
# ## Common Pitfalls
# 1. Using `=` instead of `==`
# 2. Missing colons `:`
# 3. Incorrect indentation
# 4. Overly complex conditions

# %%
# Pitfall example
x = 5
if x == 10:  # Correct comparison
    print("x is 10")

# %% [markdown]
# ## Practical Example: User Access Control
# Real-world implementation combining multiple concepts

# %%
user = {
    "username": "admin",
    "is_active": True,
    "login_attempts": 2,
    "role": "admin"
}

if user["is_active"]:
    if user["login_attempts"] < 3:
        if user["role"] == "admin":
            print("Admin dashboard")
        elif user["role"] == "editor":
            print("Editor panel")
        else:
            print("User profile")
    else:
        print("Account locked")
else:
    print("Account deactivated")
