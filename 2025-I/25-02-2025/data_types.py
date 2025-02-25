# ## Basic data types
# ### Strings
# These are sequence of characters that can be created using single or double quotes. Anything inside quotes is considered as string.

print('This is a string')
print("This is also a string")

# We can introduce anykind of character inside a string. However, in some cases we may want to apply a special meaning to a character or suppress the meaning of a special character.
#
# For this situations, we can use the backlash character `\` before the special character to 'escape' the usual meaning

# We can escape the meaning of single quote
print("Doble quotes (\") are important to build strings")

# There are other escape sequences that have a special meaning to Python:
#
# | Escape Sequence  | 	Escaped Interpretation |
# |-------------------|----------------------------|
# | \a               |	ASCII Bell (BEL) character |
# | \b |	ASCII Backspace (BS) character |
# |\f |	ASCII Formfeed (FF) character|
# |\n | ASCII Linefeed (LF) character|
# |\N{<name>} |	Character from Unicode database with given <name>|
# |\r | 	ASCII Carriage return (CR) character|
# |\t 	| ASCII Horizontal tab (TAB) character|
# |\uxxxx 	| Unicode character with 16-bit hex value xxxx|
# |\Uxxxxxxxx 	| Unicode character with 32-bit hex value xxxxxxxx|
# |\v | 	ASCII Vertical tab (VT) character|
# |\ooo |	Character with octal value ooo|
# |\xhh 	| Character with hex value hh|
#

print("We will have a new line \nafter the initial line") # Two lines


print("This introduces the \ttabulator into the string") # Tab introduced

print("\x61") #Hex

print("\N{rightwards arrow}") # Unicode by name

# The single and double quote can be used to compose strings that contain quotes inside.

print("And the police said: 'Stop there, you fool!'")

print('And the police said: "Stop there, you fool!"')

# Strings can be formatted inserting data from other variables using f-strings (f comes from format). This can be used to compose more complex strings.
#

candidate = "Luis"
score = 99.2
print(f"The candidate {candidate} got a score of: {score}")

# Like with other similar datatypes, we can know the length of a string using the function `len` and access characters using the square brackets `[]`

my_string = 'This is my string'
print(len(my_string))
print(my_string[0]) # Access the character in index 0

# The square brackets can also be used to slide the string. This logic is the same one followed when indexing lists, as it will be shown ahead.

print(my_string[8:]) # from index 8 to the end

print(my_string[-9:]) # From the one in position 9 counting from the end, until the end.

# Since a string is a sequence, we can also use the `in` and `not in` operators to know if the left-hand operand is contained in within the right-hand operand

long_string = "Abel, Luis, and Maria came to the party"
print("Luis" in long_string)
print("Roberta" in long_string)

# Some operators can be used when dealing with string values. For instance, `+` and `*` operators allow to perform concatenation and repetition:

# This is concatenation
first_string="The answer is "
second_string = "fourty two (42)"
concatenated = first_string + second_string
print(concatenated)

# This is repetition
first_string  = "And he simply said... "
second_string = "JA " * 6
repeated = first_string + second_string
print(repeated)

# As previously mentioned, a string is an object of <class 'str'>, meaning that a `str` is a class that should have its own methods.

message = "Hello WORLD!, I feel embarrassed"
print(message.title()) # Changes the string to title (Capitalize first character of each word)
print(message.upper()) # Uppercase whole string
print(message.lower()) # Lowercase whole string
print(message.swapcase()) # Swaps case of whole string
print(message.startswith("Hello")) # True if it starts with Hello
print(message.startswith("hello")) # True if it starts with Hello

# Sometimes we may need to edit our strings to remove whitespaces or prefixes.

message = "   https://helloworld.com   "
print(message) # With whitespaces
print(message.strip()) # Whitespaces removed

# Since the `str` methods return also a `str`, we can call multiple methods one after the other.

message = "   https://helloworld.com   "
print(message.strip().removeprefix('https://')) # Whitespaces and prefix removed

# Specific characters or sub-string can also be replaced with another string:

message = "BMW is a brand of vehicles"
print(message.replace("BMW", "VW")) # Replace method takes the string to replace as first argument, and the string that will replace as second argument.

# Since a string is a sequence, this can be subdivided using a particular character as separator.

message = "Augusto,Julia,Karl"
print(message.split(",")) # The split returns a list with strings that were separated by ","

# We can join again the elements of a list of strings into one sequence of characters.

message = "Augusto,Julia,Karl"
message_separated = message.split(",") # The split returns a list with strings that were separated by ","
"-".join(message_separated) # Means: join the elements of 'message_separated' using '-' as separator.

# # Exercise:
# #### Your software receives a message with data of clients that, for an unknown reason, is not in the needed format.
# #### The messages look like:
#
#     https://database.com/user/augustom,AugUSto Martin, 23, Approved,,
#     https://database.com/user/juliasch,JuLIA SchmidT, 67, rejected,,
#     https://database.com/user/kmarx,Karl Marx, 42, rejected,,
#
# #### However, your software needs to process messages like this:
#
#     message:  augustom,augustomartin,23,approved
#     message:  juliasch,juliaschmidt,67,rejected
#     message:  kmarx,karlmarx,42,rejected
#
# #### __Task__: Use `str` methods to correct the original message so you ALWAYS have messages compatible with your software.
# #### You explore the list of methods available in in `str` class [here](https://docs.python.org/3/library/stdtypes.html#textseq)

# +
# Complete the code
# -


# ### Numbers
# This can basically be integers and floats. We are allowed to use multiple operators when dealing with numbers.
#
# Operators like `+`, `-`, `*`, or `/` can be used to conduct arithmetic operations, and they are used in Python expressions.
#
# <div class="alert alert-block alert-info"><b>Hint: </b>Expressions are statements that represent a specific computation that will return a value </div>
#

2 * 3 + 2 # This expression should return 8

# We can use arithmetic operators even after assigning the numeric data to a variable.
#
# <div class="alert alert-block alert-warning"><b>Warning: </b>Data type is determined by python during runtime, meaning a number will be stored as float if it contains a decimal </div>
#

pi = 3.1416
radio = 2
print(2 * pi * radio ) # The expression is evaluated before printing

# The built-in arithmetic operators are the following:
#
# |Operator |	Name |	Example|
# |---------|------|---------|
# |+ 	|Addition 	|x + y 	|
# |- 	|Subtraction 	|x - y|
# |* 	|Multiplication |x * y |
# |/ 	|Division 	|x / y 	|
# |% 	|Modulus 	|x % y 	|
# |** 	|Exponentiation |	x ** |
# |// 	|Floor division |	x // y|
#
# <div class="alert alert-block alert-info"><b>Hint: </b>If you combine integers and floats in one operation, the resulting value will be float. </div>

print('Addition: ', 2+3)
print('Subtraction: ',2-3)
print('Multiplication: ',2*3)
print('Division: ',2/3)
print('Modulus: ',2%3)
print('Exponentiation: ',2**3)
print('Floor division: ',2//3)

# There are some python built-in methods designed to be used with numbers

print("Round: ", round(3.8))
print("Abs: ", abs(-3.8))
print("Power: ", pow(2,3))

# # Exercise:
# #### __Task__: Calculate the arclength of an angle
# #### Hint: Define an expression that will take the radius and angle as inputs
# #### __Expected result__:
# #### Diameter of circle: 9
# #### angle measure: 45
# #### Arc Length is:  3.5357142857142856

# ### Lists
#
# Lists are data structures that allow to store sets of information in one place.
# - A list is a collection of items in a __particular order__.
# - A list can contain any kind of object, from numbers, strings, to other more complex classes, or even lists.
# - In Python, lists are created using the square bracket `[]` operator, the `list()` built-in function, or a list comprehension
#

# #Using list literals
# my_list = [1,2,3,4] # Elements are separated by comma and enclosed by square brackets
# print(my_list)
# print("Object with class: ", type(my_list))
# print('List of floats: ', [1.0,3.4,5.6])
# print('List of strings: ', ['a','b','c'])
# print('List of lists: ', [['a',1],['b','c'], [2,3]]) # Each list contains elements of any type

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
print(my_list[2])

# Slices of the original list can be created using the same operator.

print(my_list[5:]) # print from 6th element until the end
print(my_list[-3:]) # Take the last three elements

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

# Elements from a list can be removed using the `del` operator and the `pop()` function.

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

# As it was initially indicated, a list is a ordered sequence. However, we can decide how to order the elements of these sequence using the `sorted()` function. 

# Sorting a list
brands = ["BMW", "VW", "renault","BMW","BMW"]
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

# One way of iterating
brands = ["BMW", "VW", "renault","BMW","BMW"]
print(f'Sorted without modifying the original list: \n{sorted(brands)}')

# Similar to the case of strings, we can use the `+` and `*` operators in lists. Well, this is obviously possible because strings are list-like objects (lists of characters). This happens because of something called [duck-typing](https://realpython.com/duck-typing-python/#duck-typing-behaving-like-a-duck), which allows to use the same methods in both `str` and `list`. We will learn more about this in the following classes.

# Operators on lists
brands_EU = ["BMW", "VW", "RENAULT","BMW","BMW"]
brands_USA= ["GMC","TESLA"]
all_brands = brands_EU + brands_USA
print(f"All brands: {all_brands}")

brands_USA= ["GMC","TESLA"]
print(f"All brands: {brands_USA * 2}")
