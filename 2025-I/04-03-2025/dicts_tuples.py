# %% [markdown]
# ### Dictionaries
#
# Dictionaries are data stuctures that allow us to connect pieces of related information. Anything that can be matched up can be stored as a dictionary Dictionaries are important python data structures becuase they can store almost limitless nested data.
# %%
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
# %%
# Accessing values in a dictionary by using the key
# Accessing the value associated with the key 'name'
print(person["name"])  # Output: John
# -

# %%
# You can also use the `get()` method to access values
print(person.get("age"))  # Output: 30


# %%
# If the key does not exist, `get()` returns None instead of raising an error
print(person.get("country"))  # Output: None

# %%
# Adding or updating key-value pairs

# Adding a new key-value pair
person["country"] = "USA"
print(person)  # Now the dictionary includes the 'country' key


# %%
# Updating an existing value
person["age"] = 31
print(person)  # The value for 'age' is updated to 31

# %%
# Using the `del` keyword
del person["city"]
print(person)  # 'city' is removed from the dictionary


# %%
# Using `pop()` to remove and return the value
age = person.pop("age")
print(person)  # 'age' is removed
print(f"Removed age: {age}")  # Output: Removed age: 31


# %%
# Checking if a key exists in a dictionary

# Using the `in` keyword
print("name" in person)  # True
print("city" in person)  # False

# %%
# Looping through a dictionary

# Iterating through keys
for key in person:
    print(key)  # Prints all keys

# %%
# Iterating through values
for value in person.values():
    print(value)  # Prints all values


# %%
# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")  # Prints key-value pairs



# %%
# We can also apply a Dictionary comprehension

# Creating a new dictionary where keys are numbers and values are their squares
squares = {x: x ** 2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}



# %%
# Nested dictionaries (dictionaries inside dictionaries)

# A dictionary containing another dictionary as a value
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 28}
}

# Accessing a nested dictionary
print(nested_dict["person1"]["name"])  # Output: Alice



# %%
# Dictionary methods

# `keys()` returns all keys as a dict_keys object
print(person.keys())  # Output: dict_keys(['name', 'country'])

# `values()` returns all values as a dict_values object
print(person.values())  # Output: dict_values(['John', 'USA'])

# `items()` returns all key-value pairs as a dict_items object
print(person.items())  # Output: dict_items([('name', 'John'), ('country', 'USA')])



# %%
# We can also use the `copy()` with dictiionaries, similar to lists.


# %%
# Using `update()` to merge another dictionary into the current one
person.update({"gender": "Male", "city": "New York"})
print(person)  # Output: {'name': 'John', 'country': 'USA', 'age': 35, 'gender': 'Male', 'city': 'New York'}


# %%
# Using the `**` unpacking operator to merge dictionaries
new_info = {"hobbies": ["Reading", "Traveling"]}
merged_dict = {**person, **new_info}
print(merged_dict)  # Output: Merged dictionary with all keys and values

# %% [markdown]
# # Tuples
# A tuple is an immutable, ordered collection of elements. They are similar to lists, but unlike lists, they cannot be modified once created.
#

# %%
# Example: Creating a tuple
my_tuple = (1, 2, 3, 4)
print(my_tuple)
# %%
# Accessing elements in a tuple

# You can access elements of a tuple by index (0-based indexing)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Negative indexing starts from the end
print(my_tuple[-1])  # Output: 4
# %%
# Slicing a tuple

# Slicing returns a new tuple with a subset of the elements
print(my_tuple[1:3])  # Output: (2, 3)

# Slicing with negative indexing
print(my_tuple[-3:-1])  # Output: (2, 3)
# %%
# Tuples are immutable, meaning their elements cannot be changed after creation

# Trying to modify an element will result in an error
try:
    my_tuple[0] = 10  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")
# %%
# Concatenating and repeating tuples

# Concatenating two tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4)

# Repeating a tuple
repeated_tuple = (5, 6) * 3
print(repeated_tuple)  # Output: (5, 6, 5, 6, 5, 6)
# %%
# Checking the length of a tuple

# Using the len() function to get the number of elements in a tuple
print(len(my_tuple))  # Output: 4 (The number of elements in my_tuple)
# %%
# Checking if an element exists in a tuple

# Using the `in` keyword
print(3 in my_tuple)  # Output: True
print(10 in my_tuple)  # Output: False
# %%
# Iterating through a tuple

# Using a for loop to iterate over the elements
for element in my_tuple:
    print(element)  # Prints each element of the tuple
# %%
# Tuple unpacking

# You can unpack the elements of a tuple into variables
a, b, c, d = my_tuple
print(a, b, c, d)  # Output: 1 2 3 4

# You can use an underscore `_` to ignore a specific value
x, _, y, _ = my_tuple
print(x, y)  # Output: 1 3
# %%
# Converting other data types to tuples

# You can convert lists, strings, and other iterable types to tuples
my_list = [1, 2, 3]
tuple_from_list = tuple(my_list)
print(tuple_from_list)  # Output: (1, 2, 3)

# Converting a string to a tuple
tuple_from_string = tuple("hello")
print(tuple_from_string)  # Output: ('h', 'e', 'l', 'l', 'o')
# %%
# Counting and finding index of elements in a tuple

# `count()` returns how many times a specified element appears in a tuple
print(my_tuple.count(3))  # Output: 1 (3 appears once)

# `index()` returns the index of the first occurrence of a specified element
print(my_tuple.index(3))  # Output: 2 (3 is at index 2)
# %%
# Creating an empty tuple

# An empty tuple can be created using empty parentheses
empty_tuple = ()
print(empty_tuple)  # Output: ()

# You can create a tuple with a single element by adding a trailing comma
single_element_tuple = (1,)
print(single_element_tuple)  # Output: (1)



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





# %%
