'''
Part 1:

    Answer these multiple choice question. You will get 1 point for each correct answer.
    Total: 10 points.
'''

'''
Q1: In Python, the type of variables are determined during runtime (dynamic typing).
What is the data type of the `division` variable after this division?
'''
division = 21/

'''
a) float
b) int
c) str
d) bool
'''

'''
Q2: What are the contents of filtered_list after this code has run:
'''
my_list = ['Porsche', 'BMW', 'Toyota',
    'Honda', 'Hyundai', 'Mazda',
    'Suzuki', 'Toyota']
filtered_list = []
for brand in my_list:
    if 'o' in brand:
        filtered_list.append(brand)
print(filtered_list)
'''
a) ['BMW', 'Hyundai', 'Suzuki', 'Mazda']
b) ['Toyota', 'Honda', 'Toyota']
c) ['Porsche', 'Hyundai', 'Suzuki', 'Mazda']
d) ['Porsche', 'Toyota', 'Honda', 'Toyota']
'''

'''
Q3: In Python, immutables types are datatypes with states that cannot mutate after created.
In other words, their values cannot and attributes cannot change during code execution.
Which of the following is NOT immutables? (more than one is valid)

a) tuple
b) int
c) set
d) dict
'''

'''
Q4: Python provides built-in methods to manipulate strings.
What is the value of `data` after this code is executed?
'''
data = 'https://database.com/user/augustom,AugUSto Martin, 23, Approved,,'
data = data.removeprefix('https://database.com/user/').lower().replace(' ','').split(',')[:-2]
print(data)
'''
a) ['augustom', 'augustomartin', '23', 'approved']
b) [' augustom', ' augustomartin', ' 23', ' approved']
c) 'augustom,augustomartin,23,approved'
d) 'augustom, augustomartin, 23, approved, ,'
'''

'''
Q5: What message do you get when you try to access
the element of index 5 of the list `my_list`?
'''
my_list = [1, 2, 'c', 'd', {'a':'b'}]
print(my_list[5])
'''
a) None
b) {'a':'b'}
c) IndexError: list index out of range
d) 'a'
'''

'''
Q6: What message do you get when you try to access
a dictionary element like this:
'''

my_dict = {
    'name':'Martin',
    'age' : 33,
    'country' : 'Luxembourg',
    'details' : None
}
print(my_dict.get('Country'))

'''
a) None
b) Luxembourg
c) KeyError: ...
d) 0
'''

'''
Q7: What is the primary purpose of the `__init__` method in a Python class?
(Just one option)

a) To initialize the class variables.
b) To be called automatically when an object of the class is created, typically used to initialize instance attributes.
c) It returns a string representation of the object.
d) It destroys an object when it's no longer referenced (garbage collection).

'''

'''
Q8: We aim to instantiate a `Wolf` class, that inherets from an abstract `Animal` class.
What is the expected output(s) from this code?
'''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hunt(self):
        pass
    @abstractmethod
    def eat(self):
        pass

class Wolf(Animal):
    def hunt(self):
        print("This animal is hunting...")
        self.eat()
        state = 'DONE'
        return state
wolf_1 = Wolf()
print(wolf_1.hunt())

'''
a) 'This animal is hunting...'
b) TypeError: Can't instantiate abstract class Wolf ...
c) 'DONE'
d)  None
'''

'''
Q9: What is the main function of a decorator in Python?

a) To add comments automatically to functions.
b) To statically type-check function arguments and return values.
c) To modify or enhance functions or methods in a clean, reusable way.
d) To define abstract base classes.
'''

'''
Q10: Consider the dictionary dishes = {'Italy': 'Pizza', 'Spain': 'Paella'}.
You want to retrieve A peruvian dish, but Peru might not be in the dictionary.
Which approach avoids a KeyError if 'Peru' is absent?

a) grades['Peru']
b) grades.get('Peru', 0)
c) grades.find('Peru')
d) grades.items()['Peru']
'''
