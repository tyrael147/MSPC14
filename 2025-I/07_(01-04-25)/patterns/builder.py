# This would be a classic way of building a burger...
class BurgerNonBuilder:
    def __init__(self, bun=None, patty=None, cheese=None):
        self.bun = bun
        self.patty = patty
        self.cheese = cheese

    def __str__(self):
        ingredients = filter(None, [self.bun, self.patty, self.cheese])
        return f"Burger with: {' + '.join(ingredients)}"

# --- Client Code ---
print("\n--- Without Builder Pattern (Using Constructor) ---")
# We need to know the parameter order or to use keywords

cheeseburger = BurgerNonBuilder(
    bun="Sesame Bun",
    patty="Beef Patty",
    cheese="Cheddar Cheese"
)
print(cheeseburger) 

simple_burger = BurgerNonBuilder(bun="Plain Bun", patty="Chicken Patty")

print(simple_burger) 

print("\n--- Using the Builder Pattern ---")

# --- Product ---
class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = None
        self.tomato = None

    def __str__(self):
        ingredients = filter(None, [self.bun, self.patty, self.cheese])
        return f"Burger with: {' + '.join(ingredients)}"

# --- Builder ---
class BurgerBuilder:
    def __init__(self):
        self._burger = Burger()

    def add_bun(self, bun_type):
        self._burger.bun = bun_type
        return self # Allows chaining

    def add_patty(self, patty_type):
        self._burger.patty = patty_type
        return self

    def add_cheese(self, cheese_type):
        self._burger.cheese = cheese_type
        return self
    
    def add_tomato(self):
        self._burger.tomato = True
        return self

    def build(self):
        return self._burger

    def take_burger(self, burger):
        self._burger = burger
        return self

# --- Client Code ---
print("--- Using Builder Pattern ---")
builder = BurgerBuilder()
cheeseburger = builder.add_bun("Sesame Bun") \
                      .add_patty("Beef Patty") \
                      .add_cheese("Cheddar Cheese") \
                      .build()

print(cheeseburger)

simple_burger = BurgerBuilder().add_bun("Plain Bun").add_patty("Chicken Patty").build()
print(simple_burger) 
# print("Excuse, I forgot to order tomato")
# modified_burger = BurgerBuilder().take_burger(simple_burger).add_tomato()
# print("This order has been modified")