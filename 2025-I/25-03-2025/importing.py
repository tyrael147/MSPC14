# # Modules and imports

# Python modules and packages help organize code into reusable components. A **module** is a `.py` file containing Python definitions (functions, classes, variables) that can be imported into other scripts.
# In contrasts, a package is a collection of modules organized in directories that include a special \_\_init\_\_.py file, signaling to Python that the directory should be treated as a package.

# ## Importing Modules/Packages
# ### **Basic Import Methods**
# | Method | Syntax | Description |
# |--------|--------|-------------|
# | **Import entire module** | `import module` | Loads the whole module |
# | **Import with alias** | `import module as alias` | Gives the module a custom name |
# | **Import specific items** | `from module import func` | Imports only selected functions/variables |
# | **Import all items** | `from module import *` | Imports everything (not recommended) |

# Importing installed modules
import math
print(math.__file__)

# Importing local modlues
import my_math
print(my_math.sum(1,2))  

# Import with alias
import my_math as mm
print(mm.multiplication(1,2))  

# Import just what is needed
from my_math import multiplication
print(multiplication(2,3))   

# Start import (DO NOT DO IT PLEASE)
from my_math import *
print(multiplication(3, 41))

# ## Module Search Path
# Python looks for modules in the following order:
# 1. Current directory
# 2. Directories in `PYTHONPATH`
# 3. Standard library paths
# 4. Site-packages directory

# Let's see all directories that python checks
import sys
print(sys.path)

# All modules have a name in the context of the run time.
print(__name__)
print(sys.__name__)

# - When a module is run directly, `__name__ == "__main__"`.
# - When imported, `__name__` is the module's name.

# If we want to run only when called directly, let's do this:
if __name__ == "__main__":
    ...
    

# # About Packages

# A **package** is a directory containing multiple modules and an `__init__.py` file.
# ```shell
# my_package/
# │
# ├── __init__.py
# ├── module1.py
# └── module2.py
# ```

import my_package 

from my_package import module1
from my_package.module2 import say_good_bye


# # Modules in a package can import each other
# Used to import modules within the same package.

# | Syntax | Description |
# |--------|-------------|
# | `from . import module` | Import from same directory |
# | `from .. import module` | Import from parent directory |

# In our package example, is we see module2.py then...
# ```python
# from . import module1
#
# ...
#
# def greeting(name):
#     module1.say_hello(name)
#     say_good_bye(name)
# ```
#

from my_package import module2
module2.greeting('name')


# **Avoid circular imports!**
#
# Add this new line at the beggining of the `module1.py` file:
# ```python
# from .module2 import say_good_bye
# ```

# Repeat it
from my_package import module2
module2.greeting('name')


# Understanding relative and absolute imports may seem a bit tricky, however you can find very nice and detailed explainations in [real python](https://realpython.com/absolute-vs-relative-python-imports/?utm_source=chatgpt.com)

# ### Built-in modules
# There are many other built-in modules that are useful in the your dailing coding.

# | Module | Purpose |
# |--------|---------|
# | `os` | Operating system interactions |
# | `sys` | System-specific functions |
# | `math` | Mathematical operations |
# | `datetime` | Date and time handling |
# | `json` | JSON data processing |
# | `pathlib` | Manage directories in an easy way |



parameters


