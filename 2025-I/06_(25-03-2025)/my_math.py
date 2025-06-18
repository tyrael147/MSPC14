"""My math module"""
import math

print('Hello world')
def sum(a,b):
    print("Here comes your sum!")
    return a + b 

def multiplication(a,b):
    print("Here comes your multiplication")
    return a * b


def my_acos(a):
    print('This is my own implementation')
    return math.acos(a)


if __name__ == "__main__":
    print("You are running this module directly.\nThis should be imported!")