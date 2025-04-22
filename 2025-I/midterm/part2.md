# Building a Burger Order System

In this exercise you will image that you are developing the software for the counter of new burger restaurant.
Customers place their orders, adding items one by one, and finally get a total bill.
Your task is to create the digital representation of a single customer order using a Python class.

# Project structure

This is the project structure:

part_2
├── run.py -> # It imports the dependencies and executes the tests
└── restaurant_system -> # Package containing the source code
    ├── orders.py -> # It contains the Order class that manages the client orders.
    ├── constants.py -> # Contains the data (names and prices).
    └── products.py -> # It contains the products' classes.

# The system:
## restaurant_system/counter.py:
This file contains the `Order` class that instantiates and order. These are required:

    Starting an Order (`__init__`):
    When a customer begins ordering and it assigns an unique `order_id` (string or integer). A new order starts empty. Design the order's constructor (i.e., `__init__`) to accept the order_id. It should also initialize an internal attribute to keep track of the items added to this specific order (e.g., a list called `self.items`).

    Adding Items (`add_item` method):
    Customers will add burgers. Implement an `add_item` method. This method should accept object of the item being added.
    Data will be stored in a dictionary like {'name': burger_name, 'price': burger_price} within the order's internal list of items.
    Items must have a cost, if the provided price is not positive (zero or negative), the method should print an error message "Item price must be positive." and not add the item to the order.
    If the price is valid, add the item details to the order and print a confirmation like ' "[Item Name]" added to order. '.

    Calculating the Total (`get_total` method):
    Once the customer is done adding items, we need to calculate the total cost. Create a `get_total` method. This method should iterate through all the items added to the order and sum up their prices. It should then return the final calculated total cost.

    Printing the Receipt (`details` method):
    We need a clear way to view the completed order, like a receipt.
    Implement `details` method. When an Order object is printed, it should return a multi-line string that should look like the following:

        Starts with Order ID: [Order ID]

        Lists each item added, one per line, formatted as - [Item Name]: $[Price].

        Ends with a line showing the Total: $[Total Price].

  ## burger_system/products.py:
  This file should contain the classes Burguer.

  For the `Burguer` class, this is required:

    Starting a `Burger` (`__init__`):
    The `__init__` constructor does not take any argument, but it defines three attributes (self.patty and self.cheese) with the `False` value.
    This constructor also creates a `self.base_price` using the data provided in the `constants.py` file.

    Adding patty(`add_patty` method):
    This method assign `True` value to self.patty when called.
    It should print a message like 'Patty added...'

    Adding cheese(`add_cheese` method):
    This method assign `True` value to self.cheese when called.
    It should print a message like 'Cheese added...'

    Calculate price (`get_price` method)
    When called, this methods calculates the price of the burguer.
    It should add the price of the patty (if added), the price of cheese (if added), and it adds them to the base price.
    Prices of cheese and patty are indicated in `constants.py`.

    Get name of burguer  (`get_name` method)
    This method returns the name of the burger.
    Base on the combinations between `self.patty`, and 'self.cheese', three options are possible: 'Cheese Burger', 'Veggie Cheese Burger', and 'Burger'

# Expected behavior:

```python

# Two clients came to the restaurant...
order1 = Order("ORD101")
order2 = Order("ORD102")

# The first client says:
# Hello, I would like a cheese burguer and a normal burguer (no cheese):
# The user of the software does this:
burguer_1 = Burguer()
burguer_1.add_patty()
burguer_1.add_cheese()
order1.add_item(burguer_1)

burguer_2 = Burguer()
burguer_2.add_patty()
order1.add_item(burguer_2)

# The order is complete.
order_1.details()

# The second client says:
# Hello, I would like a cheese burguer and a veggie burguer (no patty):
# The user of the software does this:
burguer_3 = Burguer()
burguer_3.add_patty()
burguer_3.add_cheese()
order2.add_item(burguer_3)

burguer_4 = Burguer()
burguer_4.add_cheese()
order2.add_item(burguer_4)

# The order is complete.
order2.details()
```

# Instructions

Program the system located in the part2 folder.

* This exercise gives 12 points.
* To test the solution, simply run ``python run.py`` in the terminal. If the code runs with errors and if the outputs are the same as the ones describes in ``run.py``, then solution is correct.
* The project structure has been provided.
* Some methods are incomplete (`# This is missing`), while some other parts are complete (`# This is complete`).
* Use type hints, and make comments to indicate what the line of code is doing. This will not add more points if the solution works, but it does not, I can consider extra points.
