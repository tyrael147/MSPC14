# <div class="alert alert-block alert-info"><b>hint: </b>Multiple variables can be assigned by separating the variables with a comma in left side of the assigment keyword `=`. </div>
#

from rich import print

a, b, c = 1, 2, 3
print(f' a is: {a}')
print(f' b is: {b}')
print(f' c is: {c}')

# ### Lists
#
# Lists are data structures that allow to store sets of information in one place.
# - A list is a collection of items in a __particular order__.
# - A list can contain any kind of object, from numbers, strings, to other more complex classes, or even lists.
# - In Python, lists are created using the square bracket `[]` operator, the `list()` built-in function, or a list comprehension
# - Lists can increase or decrease in size dynamically.

#Using list literals
my_list = [1,2,3,4] # Elements are separated by comma and enclosed by square brackets
print(my_list)
print("Object with class: ", type(my_list))
print('List of floats: ', [1.0,3.4,5.6])
print('List of strings: ', ['a','b','c'])
print('List of lists: ', [['a',1],['b','c'], [2,3]]) # Each list contains elements of any type

#Using list() constructor
print(list([1,2,3,4])) # it consumes an iterable or sequence
print(list("Hello World!")) # The function reads the string as a sequece (iterable)

# List can contain elements of any data type
print([1, 2.0, 'Juan']) # List contains int, float and str

# +
# List comprehension
# For later
# -


# Similar to strings, as previously mentioned, lists can be indexed using the square bracket operator.

# Print the third element
my_list = [1,34,56,6,93,12,45,67]
print(my_list)
print(my_list[2])

# Slices of the original list can be created using the same operator.

print(my_list[5:]) # print from 6th element until the end
print(my_list[-2:]) # Take the last three elements

# Once accessed, values of a list can be ingested in any other method.

brands = ["BMW", "VW", "Renault"]
print(f"The brand I like the most is {brands[2]}")

# A new element can be appended to a list using the `.append()` method.

# Using append
brands = ["BMW", "VW"]
print(f'Brands before appending: {brands}')
brands.append('Renault')
print(f'Brands after appending: {brands}')


# Elements of a list can be modified after accessing the element with the square bracket operator and assigning a new value this element

brands = ["BMW", "VW", "Renault"]
brands[0] = 'Porsche'
print(brands)

# Elements from a list can be removed using the `del` keyword and the `pop()` function.

# Using del
brands = ["BMW", "VW", "Renault"]
print('Before del: ', brands)
del brands[0]
print('After del: ', brands)

# Using pop()
# pop(i) extracts the element of index `i` and returns its value.
brands = ["BMW", "VW", "Renault"]
print('Before pop: ', brands)
popped_brand = brands.pop(0)
print('Popped brand: ', popped_brand)
print('Brands after pop: ', brands)

# when no argument is provided, it extracts the last element of the list
# Using pop()
# pop(i) extracts the element of index `i` and returns its value.
brands = ["BMW", "VW", "Renault"]
print('Before pop: ', brands)
popped_brand = brands.pop()
print('Popped brand: ', popped_brand)
print('Brands after pop: ', brands)

# List elements can also be removed by value using the `remove()` method.

brands = ["BMW", "VW", "Renault"]
print('Before remove: ', brands)
brands.remove('BMW')
print('After remove: ', brands)

# <div class="alert alert-block alert-warning"><b>Warning: </b>The `remove()` method deletes only the first occurrence of the specified value. </div>

brands = ["BMW", "VW", "Renault","BMW","BMW"]
print('Before remove: ', brands)
brands.remove('BMW')
print('After remove: ', brands)
brands.remove('BMW')
print('After remove: ', brands)
brands.remove('BMW')
print('After remove: ', brands)

# As it was initially indicated, a list is a ordered sequence. However, we can decide how to order the elements of these sequence using the `sort()` function. 

# Sorting a list
brands = ["BMWa", "VW", "renault","BMWb","BMW"]
print('Before sorting: ', brands)
brands.sort()
print('After sorting: ', brands)
brands.sort(reverse=True)
print('After sorting (reverse): ', brands)

# <div class="alert alert-block alert-warning"><b>Warning: </b>When sorting alphabetically, we must be aware that lowercase and uppercase are interpreted differently. We can convert all to lowercase to deal with this.</div>

# +
# One way of iterating
brands = ["BMW", "VW", "renault","BMW","BMW"]
print('Before lowercase: ', brands)

# We create a list using a list comprehension
brands = [name.lower() for name in brands] # we execute the method .lower() of each name in the list

print('After lowercase: ', brands)
brands.sort() # we first sort
brands = [name.upper() for name in brands] # List comprehension again
print('After sort and uppercase: ', brands) 
# -

# The previously mentioned `.sort()` sorts and modifies the state of the object that executes it.
# If you want to have a temporal sorted list, you can use the built-in method `sorted`

# +
# One way of iterating
brands = ["BMW", "VW", "renault","BMW","BMW"]

sorted_brands = sorted(brands)

print(f'Original list: \n{brands}')
print(f'Sorted without modifying the original list: \n{sorted_brands}')
# -

# Similar to the case of strings, we can use the `+` and `*` operators in lists. Well, this is obviously possible because strings are list-like objects (lists of characters). This happens because of something called [duck-typing](https://realpython.com/duck-typing-python/#duck-typing-behaving-like-a-duck), which allows to use the same methods in both `str` and `list`. We will learn more about this in the following classes.

# Operators on lists
brands_EU = ["BMW", "VW", "RENAULT","BMW","BMW"]
brands_USA= ["GMC","TESLA"]
all_brands = brands_EU + brands_USA
print(f"All brands: {all_brands}")

brands_USA= ["GMC","TESLA"]
print(f"All brands: {brands_USA * 5}")

# An important characteristic of a `list` is that it is a mutable data type because we can change the content of it.

# Operators on lists
brands_EU = ["BMW", "VW", "RENAULT","BMW","BMW"]
print(f'Original list: {brands_EU}')
print(id(brands_EU)) # Memory address of the list object


brands_EU[1]='PORSCHE'
print(f'Modified list: {brands_EU}')
print(id(brands_EU)) # The memory address is still the same

# +
brands_EU = ["BMW", "VW", "RENAULT"]
brands_EU_2 = brands_EU

print('`brands_EU_2`: ',brands_EU)
print(hex(id(brands_EU))) # We can modify the list object


# +
brands_EU.append("PEUGEOT")
# When we call the variable 'brands_EU_2', we are referencing to the same object in 'brands_EU'
print('`brands_EU_2`: ',brands_EU_2)

print(hex(id(brands_EU_2))) 
# -

# In some situations, we may want to create a copy of a `list` and modify it without affecting the content of the original list. 

# We can first make a `shallow` copy, which creates a new list containing the references to objects contained in the original list. This can be done by:
# * Using the slicing operator [:] (you already know this)
# * Using the `.copy()` method
# * Using the `copy()` method from the copy module

brands_EU = ["BMW", "VW", "RENAULT"]
print(brands_EU[:])


brands_EU = ["BMW", "VW", "RENAULT"]
brands_USA = ["TESLA", "FORD"]
brands_cars = [brands_EU, brands_USA]
print(brands_cars) # Lists of lists

# Using the .copy() method
brands_cars_copied = brands_cars.copy()
print(brands_cars_copied)

# +
# Using the .copy() method
#brands_cars_copied = brands_cars.copy()

#You can also use the copy method from the copy module
from copy import copy
brands_cars_copied = copy(brands_cars)

print('`brands_cars` id: ',hex(id(brands_cars)))
print('`brands_cars_copied`: ',hex(id(brands_cars_copied)))
# Let's verify if the first element of each list.
# Are they refering to the same object?
# -

# If we modify the one of the elements of the original list the new list won't be affected
brands_cars_copied[1] = ['TOYOTA',"NISSAN"]
print(brands_cars)
print(brands_cars_copied)

# If we modify the elements of one of the elements, what would happen?
brands_cars[0][2] = "FIAT"
print(brands_cars)

print(brands_cars_copied)

brands_cars_copied[0][2] = "CITROEN"

print(brands_cars)
print(brands_cars_copied)

# When we want to make a complete copy of a `list` we will need to make a __deep copy__. This approach creates copies of each element of the object recursively. 

# +
from copy import deepcopy

brands_EU = ["BMW", "VW", "RENAULT"]
brands_USA = ["TESLA", "FORD"]
brands_cars = [brands_EU, brands_USA]

brands_cars_deep_copied = deepcopy(brands_cars)

# Verifying the id of the lists
print('`brands_cars` id: ',hex(id(brands_cars)))
print('`brands_cars_deep_copied`: ',hex(id(brands_cars_deep_copied)))

# Verifying the id of the first object contained in the lists

print('`brands_cars[0]` id: ',hex(id(brands_cars[0])))
print('`brands_cars_deep_copied[0]` id: ',hex(id(brands_cars_deep_copied[0])))


# +
# When we modify one of the elements of the new list it does not affect the original list
print('Original deep copy: ', brands_cars_deep_copied)
brands_cars_deep_copied[1][0] = 'GMC'
print('New deep copy: ', brands_cars_deep_copied)

print('Original list: ', brands_cars) # This was never affected
# -

# You can find more `list` methods in the python documentation [here](https://docs.python.org/3/tutorial/datastructures.html)

# #### About mutables and immutables
# The data types that we have seen before (e.g., str, int) differ from mutables since they are IMMUTABLE. They cannot be modified once created. You will also note that immutable objects have methods that return a new object, instead of methods that modify the state.
#

my_string = "PEUGEOT"
my_string[1] = "e"

my_string = "PEUGEOT"
print(my_string)
print(id(my_string))
my_string = my_string.lower()
print(my_string)
print(id(my_string))

# <div class="alert alert-block alert-warning"><b>Warning: </b>In python, we must distinguish the difference between the name (or variable) and the object. Many names or variables can refer to the same object. Most python built-in types are immutable, so we cannot modify the object, but just create new objects from the old one and assign it to the same or a new variable.</div>

# <div class="alert alert-block alert-info"><b>hint: </b>There three characteristics that we need to know when observing a python object: value, identity, type.</div>

my_variable = "This is a nice string"
print(f'The value: {my_variable}')
print(f"The identity: {id(my_variable)}")
print(f"The type: {type(my_variable)}")


# We can verify the type 
isinstance(my_variable,str)

# ### Looping through a sequence
# As mentioned before, a `list` is a sequence of objects in a particular order. In python, we commonly want to go through each element of this `list` and execute tasks. The traversing of list can be done using different constructs, the most common however are `for` loops and list comprehensions.

# #### Using `for` loops
# The `for` keyword can be used to iterate over a sequence a fixed number of times. This keyword must always be used in combination with an iterable object. `for` iterates over the members of the sequence __in order__, executing the code block each time. The `for` keyword is used in combination with the `in` keyword.

brands_EU = ["BMW", "VW", "RENAULT","CITROEN","FIAT"]
# The pattern is `for` <variable> `in` <sequence>: <code block>
for brand in brands_EU:
    print(brand)


# We can iterate through any sequence
for letter in brands_EU[0]:
    print(letter)

# We can build nested iterations if necessary. We need to repeat the \` `for` \<variable\> `in` \<sequence\>: \<code block\> \` pattern, being careful of the indentation, which defines the scope of the for-loop.

brands_EU = ["BMW", "VW", "RENAULT","CITROEN","FIAT"]
# The pattern is `for` <variable> `in` <sequence>: <code block>
for brand in brands_EU: # 5 elements
    my_variable = 'happy'
    # print(f"This is the brand: {brand}")
    # we repeat the pattern
    for letter in brand: # 3, #2, 
        # print(f"This is a letter: {letter}")
        ...


# In some situations, we also want to know the index location of the current variable. For this, we can use the built-in function `enumerate`, which takes an iterable and returns an iterator that yields a two-items tuple on demand.

brands_EU = ["BMW", "VW", "RENAULT","CITROEN","FIAT"]
# The pattern is `for` <variable> `in` <sequence>: <code block>
for index, brand in enumerate(brands_EU): # enumerate() returns two objects: the index and the value
    
    print(f"This is the brand: {brand} located in the {index} place")


# <div class="alert alert-block alert-warning"><b>Warning: </b>enumerate() creates an iterator that returns two objects after every loop. Different from a sequence, where all the elements of the sequence are already in memory, an iterator yields values progressively, on demand </div>

# We do not get the 
enumerate(brands_EU)

# We can also perform tasks that modify the state of the original list

# +
brands_EU = ["BMW", "VW", "RENAULT","CITROEN","FIAT"]

for index, brand in enumerate(brands_EU):
    brands_EU[index] = brand.lower() # We modify the string located in the position `index`
    print(brands_EU)
# -

# The `for` loop will iterate until exhausting the list. In some cases we may want to stop the iteration after some condition is met. For this we use the `break` keyword.

# +
brands_EU = ["BMW", "VW", "RENAULT","CITROEN","FIAT"]

for brand in brands_EU:
    
    print(f"This is the brand: {brand}")

    if brand == "RENAULT": # Condition introduced
        print("Condition met, stopping loop")
        break
    # we repeat the pattern
    for letter in brand:
        print(f"This is a letter: {letter}")

# -

# <div class="alert alert-block alert-info"><b>hint: </b>The `if` keyword is used to introduce a condition. 
#     The pattern is `if` < expression > : < code-block >. The < code-block > will be executed only if the expression is `True`. </div>

# This expression... :
if 1 in [1,2,3]:
    print("All good")

# Is equivalent to... :
if True:
    print("All good")

# Similarly to the previous case, we can skip the code block given some condition without stopping the whole iteration. For this, we use the `continue` keyword.

# +
brands_EU = ["BMW", "VW", "RENAULT","CITROEN","FIAT"]

for brand in brands_EU:
    
    if brand == "RENAULT": # Condition introduced
        print("Condition met, skipping this brand")
        continue    
    print(f"This is the brand: {brand}")



# -

# A fast way to create a list of number is by using the built-in method `range()`. It allows us to create a list of numbers. This method is commonly used with for-loops.

for i in range(0,10): # create 10 sequential integers from 0 to 10
    print(i)

for i in range(0,10,2): # create 10 sequential integers from 0 to 10, every two steps
    print(i)

print(list(range(0,10)))
print(sum(range(0,10)))
print(min(range(0,10)))
print(max(range(0,10)))

# <div class="alert alert-block alert-info"><b>hint: </b>The For-loop constructs is present in many programming languages with different syntax. In other programming languages you may need to define expressions to control the next loop value, or an expression to determine if the loop is done. In Python, this is controlled by building the appropiate sequence. </div>

# #### Usuing list comprehension for looping
# Lists comprehensions are a particular construct of python and they allow us to iterate through lists with one simple line of code. The main difference from for looping is that list comprehensions are designed to create a list through the iteration of another list. A list comprehension combines the for-loop and the creation of new elements into one line. This is an advanced way of building lists, but you will probably find them in many python files out there.

# +
# For looping and built-in methods for modifying lists
brands_EU = ["BMW", "VW", "RENAULT","CITROEN","FIAT"]
selected = []

for brand in brands_EU:
    if 'W' in brand: # Condition introduced
        selected.append(brand)      

print(f"This is the new list: {selected}")

# +
# Using list comprehension

# The pattern is [<variable_1> for <variable_1> in <a sequence> <condition>]
selected = [brand for brand in brands_EU if 'R' in brand]

print(f"This is the new list: {selected}")

# +
# We can also do nested iterations with list comprehension
brands_EU = ["BMW", "VW", "RENAULT"]
brands_USA= ["GMC","TESLA","FORD"]
all_brands = [brands_EU, brands_USA]
print(f"All brands: {all_brands}")

# Using for loops
selected = []
for brand_list in all_brands:
    for brand in brand_list:
        if "L" in brand:
            selected.append(brand)
print('Using for loops: ',selected)

# Using list comprehension

selected_1 = [brand for brand_list in all_brands for brand in brand_list if "L" in brand ]

print('Using list comprehension: ',selected_1)


# -

# ## Exercise
# Let's practice some list comprehension. These tasks were taken from [here](https://gist.github.com/ryanorsinger/f7d7c1dd6a328730c04f3dc5c5c69f3a) (go and give him a star ;)).

# +
# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# -

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']


# Exercise 5 - make a list that contains each fruit with more than 5 characters


# Exercise 6 - make a list that contains each fruit with exactly 5 characters


# Exercise 7 - Make a list that contains fruits that have less than 5 characters


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"


# +
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
# -

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers


# # When to use list comprehension and when to use for loops?

import this


