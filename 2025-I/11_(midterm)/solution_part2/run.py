from restaurant_system.products import Burger
from restaurant_system.counter import Order

def test_1():
    order1 = Order("ORD101")

    # The first client says:
    # Hello, I would like a cheese burger and a normal burger (no cheese):
    # The user of the software does this:
    burger_1 = Burger()
    burger_1.add_patty()
    burger_1.add_cheese()
    order1.add_item(burger_1)

    burger_2 = Burger()
    burger_2.add_patty()
    order1.add_item(burger_2)

    # The order is complete.
    order1.details()

def test_2():
    order2 = Order("ORD102")
    # The second client says:
    # Hello, I would like a cheese burger and a veggie burger (no patty):
    # The user of the software does this:
    burger_3 = Burger()
    burger_3.add_patty()
    burger_3.add_cheese()
    order2.add_item(burger_3)

    burger_4 = Burger()
    burger_4.add_cheese()
    order2.add_item(burger_4)

    # The order is complete.
    order2.details()

if __name__=='__main__':
    test_1()
    test_2()

'''
Output should be :

> python run.py

Order ORD101 started.
Order ORD102 started.
Patty added...
Cheese added...
"Cheese Burger" added to order.
Patty added...
"Burger" added to order.
Order ID: ORD101

- Cheese Burger: $1.30
- Burger: $1.20
Total: $2.50
Patty added...
Cheese added...
"Cheese Burger" added to order.
Cheese added...
"Veggie Cheese Burger" added to order.
Order ID: ORD102

- Cheese Burger: $1.30
- Veggie Cheese Burger: $0.90
Total: $2.20
'''
