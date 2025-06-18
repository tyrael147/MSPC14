# %% [markdown]
# # Introduction
# In this first introductory section we will learn the basic of variables and python data types.
# To execute this file correctly, be sure to install the required dependencies listed in the [requirements.txt](requirements.txt) file.
#
# This jupyter notebook (`*.ipynb`) allows us to execute code cell-by-cell interactively, different from python files (with the .py extension) from which code is executed in one step ([more here](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html)).
#
# <div class="alert alert-block alert-warning"><b>Warning: </b>Python files are not executed automatically by jupyterlab. If you want to open a python file *.py you should `Open with notebook`.</div>
#

# %% [markdown]
# ## Variables
#
# Variables are symbolic names that point to objects in memory.
# In other words, they are connected to a value, which is the data associated with the respective variable.
# Variables can be created using the assignment operator (`=`).
#
# <div class="alert alert-block alert-info"><b>Hint: </b>Execute cells doing `Ctrl+Enter`, or Execute cells and go to the next one doing `Shift+Enter`</div>
#
# <div class="alert alert-block alert-info"><b>Hint: </b>If you do not want to execute a line, comment it preceding the line with `#`</div>
#

# %%
from rich import print 

# %%
# This line is a comment
# We assign a string to the variable 'message'
message = "Hello to all!"
# We assign an int to the variable 'number'
number = 42.0
print("The message is: ", message)
print("The number is: ", number)

# %% [markdown]
# We can verify the data types using the function type(). This function return the class of the object.

# %%
print("Type of 'message': ",type(message))
print("Type of 'number': ", type(number))

# %% [markdown]
# Both `message` and `number` variables have their own address in the computer memory.
# To access to this address, we can use the built-in `id()` function.
# This function returns the “identity” of an object. This `id` is an unique integer that is constant for this object during the interpreter lifetime.

# %%
id(message)

# %%
print('Address of "message": ', hex(id(message)))
print('Address of "number": ', hex(id(number)))

# %% [markdown]
# If we assign the variable 'message' to the new variable 'new_message', this later will point to the address of the original data.

# %%
new_message = message # We assign one more time.
print('Address of "message": ', hex(id(message)))
print('Address of "new_message": ', hex(id(new_message)))


# %% [markdown]
# When creating variables we need to consider some particular rules and guidelines.
# <div class="alert alert-block alert-warning"><b>Warning: </b>Names can only contain letters, numbers, and underscores. They can start with a letter or underscore, but never with a number </div>
#
#

# %%
_1_message = "hello" # This does not work

# %% [markdown]
# <div class="alert alert-block alert-warning"><b>Warning: </b>Spaces are not allowed as part of names.</div>
#

# %%
my_variable = 1 # This does not work

# %% [markdown]
# <div class="alert alert-block alert-warning"><b>Warning: </b>There are some Python keywords that are not forbidden but should be avoided (see here: https://docs.python.org/3/library/functions.html) </div>
#

# %%
# print = 12 # This should always be avoided
# print() # This does not work

# %%
print("hello world")

# %% [markdown]
# <div class="alert alert-block alert-info"><b>Hint: </b>Use short but descriptive names </div>
#

# %%
n="John" # This is not recommended
name="John" # This is better
length_of_persons_name = 23 # This is not recommmended
name_length = 23 # This is better

# %%
print(name_length)

# %% [markdown]
# <div class="alert alert-block alert-danger"><b>Warning: </b>The most common mistake when learning programming are spelling mistakes when calling variables. Luckily, Python provides means to identify this type of errors</div>
#

# %%
my_message = "This is my message"
print(my_message) # This should drop a NameError, 'my_mesage' is obviously not defined because I made a typo.

# %%
