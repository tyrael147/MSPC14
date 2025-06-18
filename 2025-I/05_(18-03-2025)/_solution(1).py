# # Solution: Shopping system

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - ${self.price:.2f}")


class ShoppingCart:
    def __init__(self):
        self._items = {}  # Format: {product.name: {"product": product, "quantity": quantity}}

    def add_product(self, product, quantity=1):
        if product.name in self._items:
            self._items[product.name]["quantity"] += quantity
        else:
            self._items[product.name] = {"product": product, "quantity": quantity}

    def remove_product(self, product, quantity=1):
        if product.name in self._items:
            if self._items[product.name]["quantity"] > quantity:
                self._items[product.name]["quantity"] -= quantity
            else:
                del self._items[product.name]
        else:
            print(f"Error: {product.name} is not in the cart.")

    def calculate_total(self):
        total = 0.0
        for item in self._items.values():
            total += item["product"].price * item["quantity"]
        return total

    def display_cart(self):
        print("Shopping Cart:")
        for name, item in self._items.items():
            print(f"{item['quantity']} x {name} - {item['product'].price} each")
        print(f"Total: {self.calculate_total()}\n")


# +

# Test the implementation
# Create products
apple = Product("Apple", 0.99)
banana = Product("Banana", 0.59)
milk = Product("Milk", 3.49)

# Create cart
cart = ShoppingCart()

# Add items
cart.add_product(apple, 3)
cart.add_product(banana)
cart.add_product(milk, 2)
cart.display_cart()

# Remove items
cart.remove_product(apple, 1)
cart.remove_product(banana)
cart.display_cart()

# Try to remove a product not in the cart
cart.remove_product(milk, 5)  # Removes all milk
cart.display_cart()
# -

# # Solution: Library system

# +

class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._checked_out = False

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def isbn(self):
        return self._isbn  # Read-only (no setter)

    @property
    def checked_out(self):
        return self._checked_out

    def check_out(self):
        if not self._checked_out:
            self._checked_out = True
            return True
        print(f"Book '{self._title}' is already checked out.")
        return False

    def check_in(self):
        if self._checked_out:
            self._checked_out = False
            return True
        print(f"Book '{self._title}' is already checked in.")
        return False

    def display_info(self):
        status = "Checked Out" if self._checked_out else "Available"
        print(f"Title: {self._title}\nAuthor: {self._author}\nISBN: {self._isbn}\nStatus: {status}\n")


# -

class Customer:
    def __init__(self, name, customer_id):
        self._name = name
        self._customer_id = customer_id
        self._checked_out_books = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def checked_out_books(self):
        return self._checked_out_books

    def check_out_book(self, book):
        if book.check_out():
            self._checked_out_books.append(book)
            print(f"Book '{book.title}' checked out to {self._name}.")

    def check_in_book(self, book):
        if book in self._checked_out_books:
            book.check_in()
            self._checked_out_books.remove(book)
            print(f"Book '{book.title}' checked in from {self._name}.")
        else:
            print(f"Book '{book.title}' not found in {self._name}'s list.")

    def display_info(self):
        print(f"Customer Name: {self._name}\nID: {self._customer_id}")
        print("Checked Out Books:")
        for book in self._checked_out_books:
            print(f"- {book.title}")


class Library:
    def __init__(self):
        self._books = []
        self._customers = []

    def add_book(self, book):
        self._books.append(book)

    def add_customer(self, customer):
        self._customers.append(customer)

    def find_book(self, isbn):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def find_customer(self, customer_id):
        for customer in self._customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def check_out_book(self, customer_id, isbn):
        customer = self.find_customer(customer_id)
        book = self.find_book(isbn)
        if not customer:
            print("Customer not found.")
            return
        if not book:
            print("Book not found.")
            return
        customer.check_out_book(book)

    def check_in_book(self, customer_id, isbn):
        customer = self.find_customer(customer_id)
        book = self.find_book(isbn)
        if not customer:
            print("Customer not found.")
            return
        if not book:
            print("Book not found.")
            return
        customer.check_in_book(book)

    def display_books(self):
        print("Library Books:")
        for book in self._books:
            book.display_info()

    def display_customers(self):
        print("Library Customers:")
        for customer in self._customers:
            customer.display_info()
            print()


# +
# Test the implementation
# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")

# Create customers
customer1 = Customer("Alice Smith", "C001")
customer2 = Customer("Bob Johnson", "C002")

# Create library
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_customer(customer1)
library.add_customer(customer2)

# Perform check-outs
library.check_out_book("C001", "9780743273565")  # Alice checks out The Great Gatsby
library.check_out_book("C001", "9780451524935")  # Alice checks out 1984
library.check_out_book("C002", "9780743273565")  # Bob tries to check out an already checked-out book

# Display info
library.display_books()
library.display_customers()

# Perform check-ins
library.check_in_book("C001", "9780743273565")  # Alice returns The Great Gatsby
library.check_in_book("C002", "9780743273565")  # Bob tries to return a book he didn't check out

# Display updated info
library.display_books()

# -


