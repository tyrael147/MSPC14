from . import module1


def say_good_bye(name):
    print(f'Good bye {name}!')

def greeting(name):
    print('This is a proper greeting')
    module1.say_hello(name)
    say_good_bye(name)