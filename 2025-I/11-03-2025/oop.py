# %% [markdown]
# # Object-Oriented Programming (OOP) in Python
# Object-Oriented Programming (OOP) is a programming paradigm in which a program is structured in a way so that data and behaviors are contained into elements named 'objects'.
#
# In OOP, we write *classes* that may represent real-world elements or situations and we create *objects* based on these *classes*.
# When we write a ``class``, we define the general behavior and data that a whole category of object can have. 
#
# In other words:
#
# ***A class is a blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) of the objects***.

# %%
from rich import print


# %%
# Example of a simple class:

class Dog: # We use the class keyword
    
    # Constructor method (initializer)
    # The `self` argument is required and it must come first.
    # `self` is a reference to the instance that will be created from this class
    def __init__(self, name, age):
        self.name = name  # Instance variable, also called attribute
        self.age = age    # It is specific to each object and it will accessed by the instance 

    # Method that makes the dog bark
    def bark(self):
        return f"{self.name} is barking: woof!"
        
    # Method to get the dog's age
    def get_age(self):
        return self.age

    # Create a 'sit' method that prints the name of the dog and the message: ... is sitting 

# %%
# Creating object from a class is called `instantiation`

dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Accessing methods and attributes
print(dog1.bark())  
print(dog2.get_age())  
# print(dog1.sit())
# print(dog1.name)

# %% [markdown]
# <div class="alertaalert-block alert-info">
# ⚠️ <b>Important: </b> The __init__ method is a special method that is called by python every time we instantiate  a class.
# </div>
#

# %% [markdown]
# <div class="alertaalert-block alert-info">
# ⚠️ <b>Hint: </b>Special methods are also called magic or dunder methods. These have double leading and trailing underscores. The underscores convention serve to flag the methods as core of some Python features.
# </div>
#

# %% [markdown]
# <div class="alertaalert-block alert-warning">
# While we can define or override magic methods, these are <b>NOT</b> intented for direct use. We should not call them directly, but let Python call them automatically</div>
#

# %% [markdown]
# Some dunder methods:
#
# | Special Method       | Description                                      |
# |----------------------|--------------------------------------------------|
# | `__init__()`        | Provides an initializer in Python classes        |
# | `__str__()` and `__repr__()` | Provide string representations for objects |
# | `__call__()`        | Makes the instances of a class callable          |
# | `__len__()`         | Supports the `len()` function                     |
#
# Learn more about magic methods [here](https://realpython.com/python-magic-methods) and [here](https://docs.python.org/3/reference/datamodel.html#specialnames)

# %%
# Instance variables are specific to each object, while class variables are shared across all instances of the class.
class Car:
    # Class variable
    wheels = [4] # Every car has 4 wheels by default

    def __init__(self, brand, model):
        # Instance variables
        self.brand = brand
        self.model = model

# Creating two car objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.wheels)  
print(car2.wheels)  
print(car1.model)    
print(car2.model)    

# %%
# If we change wheels and model of car1, what will happen?
car1.wheels.append(2)
car1.model = 'Yaris'

# %%
print(car1.wheels)
print(car2.wheels)
print(car1.model)
print(car2.model)


# %% [markdown]
# # Task
#
#
# Create a `Car` class and implement methods to:
#
# - Register owner, brand, model, and engine size when instantiating.
# - Modify the engine size.
# - Modify the name of the owner
# - Retrieve the state of the car, for example "This car is a *Renault* model *Clio* and it belongs to *Gustavo Larrea*.
#
#

# %%
# Your code here

class Car:

    ...



# %% [markdown]
# ## Python supports four main OOP principles:
#
# There are four main principles that are the basis of OOP in python:
#
# - **Inheritance**
# - **Polymorphism**
# - **Encapsulation**
# - **Abstraction**
#

# %% [markdown]
# ### Inheritance
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). 
# This promotes code reuse and hierarchical relationships.
#
# **Example:**
# - A `Vehicle` class is created as a parent class.
# - A `Car` class inherits from `Vehicle` and extends its functionality.
#

# %%
# Parent class (Vehicle)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"The {self.model} engine is now running."

# A child class (Car) that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # Calling the constructor of the parent class
        super().__init__(brand, model)
        self.doors = doors  # Adding new attribute specific to Car

    def honk(self):
        return f"The {self.model} honked its horn!"

# Creating an object of Car (child class)
car = Car("Tesla", "Model S", 4)

#We can access methods defined in both the child and the parent classes
print(car.start_engine()) 
print(car.honk())
print(car.brand) 

# %% [markdown]
# <div class="alertaalert-block alert-info">
# ⚠️ <b>Hint: </b>The super() method returns a temporary object of the parent class that allows us to call methods from the superclass. This built-in method is fundamental when doing inherentance in Python.
# </div>
#

# %% [markdown]
# Learn more about `super()` [here](https://realpython.com/python-super/) and [here](https://docs.python.org/3/library/functions.html#super).

# %% [markdown]
# ### Polymorphism
# Polymorphism is a concept in which we treat objects of different types as if they were instance of the same type as long as they have implemented the same interface or behavior. 
# In other words, through polymorphism, we are allow different classes to have methods with the same name but different implementations.
#
# **Example:** 
#
# - Both `Dog` and `Cat` have a `make_sound()` method, but `Dog` returns `"Woof"` and `Cat` returns `"Meow"`.

# %%
class Cat:
    def make_sound(self):
        return "Meow"

class Dog:
    def make_sound(self):
        return "Woof"

# Function that demonstrates polymorphism
# We do not care of the class of animal, we only care that it can make a sound
def animal_sound(animal):
    print(animal.make_sound())

# Creating objects
cat = Cat()
dog = Dog()

# Passing different objects to the same function
animal_sound(cat)
animal_sound(dog)

# %% [markdown]
# ### Encapsulation:
#
#
# Encapsulation is the concept of bundling data and behaviors that operate on the data into a single element (in other words, a class).
# The general idea that encapsulation promotes is to implement methods to protect object state and data from the outside by limiting the direct access.
#
#
# **Example:**
# A class `BankAccount` can have a private `balance` and public methods like `deposit()` or `withdraw()` to manipulate it.

# %%
class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.__owner = owner
        self.__balance = balance  # This is private attribute because it has double underscore
        self._account_number = account_number # This is protected attribute so it shouldn't be accessed directly
        
    # Method to deposit money
    def deposit(self, amount):
        self.__balance += amount
        self._log_transaction(f"Deposited: {amount}")
    
    
    # Protected method (convention: internal use only)
    def _log_transaction(self, message):  # Single underscore prefix
        print(f"Transaction Log: {message} - Balance: {self.__balance}")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self._log_transaction(f"Withdrew: {amount}")

    # Method to get the current balance
    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

# Creating a BankAccount object
account = BankAccount("Alice", 1000)

# Using public methods to interact with private data
print(account.deposit(500)) 
print(account.withdraw(200)) 
print(account.get_balance()) 
print(account.get_owner()) 

# %%
# type . next to `account`, then press tab and try to find the _log_transaction() method
account

# %%
# Trying to access the private variable directly will raise an error
print(account.__balance)  # This will raise an AttributeError

# %% [markdown]
# <div class="alertaalert-block alert-info">
# ⚠️ <b>Info: </b>Unlike some other languages like Java, Python does not use explicit access keywords like `private` or `public`. Instead, Python uses naming conventions. A single leading underscore means that a variable is intended to be private, but it is still accessible. Double leading underscores invoke name mangling to make it harder to access from outside the class.
# </div>
#

# %%
dir(account)

# %% [markdown]
# ### Abstraction:
#
# Abstraction is the concept of hiding the complexity of implementation details and showing only essential features of an object. 
# An abstraction enforces a consistent interface, helping developers to focus on what the object does, rather than how it does it.
#
# **Example:**
#
# When you use a `Car` object, you don’t need to know how the engine works internally; you just call methods like `start()` or `stop()`.

# %%
# For abstraction we need to use the `abc` module.
# An abstract class cannot be instantiated and requires subclasses to implement abstract methods.

from abc import ABC, abstractmethod

# ABC parent is used to create an abstract class
# The Animal class cannot be instantiated directly, it is meant to be inhereted

class Animal(ABC):
    # The decorator @abstractmethod is used to indicate that the method is abstract
    # The method does not provide any implementation but it enforces its implementation in subclasses
    @abstractmethod 
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

dog = Dog()
print(dog.make_sound())  # Output: Woof

# %%
# Try to implement a Dog class without the make_sound() method


# %% [markdown]
# # What are the advantages of OOP?
#
# **Modularity**: Code is organized into classes and objects, making it easier to maintain and update.
#
# **Code Reusability**: Inheritance allows one class to inherit the behavior of another.
#
# **Maintainability**: Encapsulation helps in hiding internal data, reducing the chances of accidental modification.
#
# **Flexibility and Scalability**: Polymorphism allows for a unified approach to dealing with different types of objects.

# %%
