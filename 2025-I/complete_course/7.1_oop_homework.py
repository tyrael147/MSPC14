# %% [markdown]
#
# # Homework
# ## Use the concepts explained before (e.g., inheritance, polymorphism, encapsulation and composition) to model a farm ecosystems.
#
# ## You should consider the following:
#
# 1. Implement an Animal abstract base class with:
#
#         * Attributes: name (str), age (int)
#
#         * Abstract method: make_sound()
#
#         * Concrete method: feed() (prints feeding confirmation)
#
# 2. Create at least 3 animal subclasses (e.g., Cow, Chicken, Sheep) with:
#
#         * Unique implementations of make_sound()
#
#         * At least one specialized method per subclass (e.g., milk(), lay_egg(), shear())
#
# 3. Design a Farm class that:
#
#         * Manages a collection of animals and farm structures (e.g., barns, coops)
#
#         * Create methods to add/remove animals and structures
#
#         * Implement a method to feed animals and collect products called `daily_routine()`
#
#         * Implement the methods `list_structures()` and `show_population()` to display farm structure and animal population, respectively.
#
# 4. Include a FarmStructure class to represent buildings with:
#
#         * Attributes: name, type (e.g., "Barn", "Coop")
#
#         * A method to describe the structure
# 5. Demonstrate polymorphism by iterating through animals to trigger make_sound(), and encapsulation by keeping internal data private where appropriate.
#

# %% [markdown]
# # Output
# Imagine that you create a farm instance:
# ```python
# my_farm = Farm(...)
# my_farm.show_population()
#
# #Output:
# Welcome to The Belval Farm!  
# Farm Population:  
# - Cow: 2  
# - Chicken: 3  
# - Sheep: 5  
# ```
#
#
# ```python
# my_farm = Farm(...)
# my_farm.list_structures()
#
# #Output
# Structures:  
# Red Barn (Barn)  
# Hen Palace (Coop)  
# ```
#
# ```python
# my_farm = Farm(...)
# my_farm.daily_routine()
#
# #Output
#  ----- Morning Routine ------
# Bessie is being fed!  
# Clucker is being fed!  
# ...  
# Collected products: Milk, Egg, Wool  
# ```


# %%
