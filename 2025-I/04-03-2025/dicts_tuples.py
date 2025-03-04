# ### Dictionaries
#
# Dictionaries are data stuctures that allow us to connect pieces of related information. Anything that can be matched up can be stored as a dictionary Dictionaries are important python data structures becuase they can store almost limitless nested data.

# +
# A dictionary is a collection of key-value pairs.
# Each key is unique, and the value can be any data type (int, string, list, etc.)

# Example: Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Print the dictionary
print(person)


# +
# Accessing values in a dictionary by using the key

# Accessing the value associated with the key 'name'
print(person["name"])  # Output: John
# -

# You can also use the `get()` method to access values
print(person.get("age"))  # Output: 30

# If the key does not exist, `get()` returns None instead of raising an error
print(person.get("country"))  # Output: None

# +
# %%
# Adding or updating key-value pairs

# Adding a new key-value pair
person["country"] = "USA"
print(person)  # Now the dictionary includes the 'country' key

# -

# Updating an existing value
person["age"] = 31
print(person)  # The value for 'age' is updated to 31


# Using the `del` keyword
del person["city"]
print(person)  # 'city' is removed from the dictionary


# Using `pop()` to remove and return the value
age = person.pop("age")
print(person)  # 'age' is removed
print(f"Removed age: {age}")  # Output: Removed age: 31

# +
# Checking if a key exists in a dictionary

# Using the `in` keyword
print("name" in person)  # True
print("city" in person)  # False


# +
# Looping through a dictionary

# Iterating through keys
for key in person:
    print(key)  # Prints all keys

# Iterating through values
for value in person.values():
    print(value)  # Prints all values

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")  # Prints key-value pairs


# +
# Dictionary comprehension

# Creating a new dictionary where keys are numbers and values are their squares
squares = {x: x ** 2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# +
# Nested dictionaries (dictionaries inside dictionaries)

# A dictionary containing another dictionary as a value
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 28}
}

# Accessing a nested dictionary
print(nested_dict["person1"]["name"])  # Output: Alice


# +
# Dictionary methods

# `keys()` returns all keys as a dict_keys object
print(person.keys())  # Output: dict_keys(['name', 'country'])

# `values()` returns all values as a dict_values object
print(person.values())  # Output: dict_values(['John', 'USA'])

# `items()` returns all key-value pairs as a dict_items object
print(person.items())  # Output: dict_items([('name', 'John'), ('country', 'USA')])


# +
# We can also use the `copy()` with dictiionaries, similar to lists.

# +
# %%
# Merging two dictionaries (Python 3.5+)

# Using `update()` to merge another dictionary into the current one
person.update({"gender": "Male", "city": "New York"})
print(person)  # Output: {'name': 'John', 'country': 'USA', 'age': 35, 'gender': 'Male', 'city': 'New York'}

# Using the `**` unpacking operator to merge dictionaries
new_info = {"hobbies": ["Reading", "Traveling"]}
merged_dict = {**person, **new_info}
print(merged_dict)  # Output: Merged dictionary with all keys and values

# -

# ## Homework

# You are given a list of dictionaries, where each dictionary represents a student and contains their name and a list of grades. Write a Python function that:
#
# * Iterates through the list of dictionaries.
# * For each student, calculates their average grade.
# * It sorts the grade.
# * Adds a new key to the dictionary named 'average' that stores their average grade.
# * Returns a list of dictionaries with the students' names and their average grades.
#
# Input
# ```
# students = [
#     {'name': 'Alice', 'grades': [90, 85, 92]},
#     {'name': 'Bob', 'grades': [70, 88, 80]},
#     {'name': 'Charlie', 'grades': [95, 93, 97]}
# ]
# ```
# Output
# ```
# [
#     {'name': 'Alice', 'grades': [85, 90, 92], 'average': 89.0},
#     {'name': 'Bob', 'grades': [70, 80, 88], 'average': 79.33},
#     {'name': 'Charlie', 'grades': [97, 95, 93], 'average': 95.0}
# ]
# ```
#




