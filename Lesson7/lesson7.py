import requests
import colorama
from colorama import Fore
def foo():
    pass


class Human:
    def __init__(self, age, height, name="Vlad"):
        self.age = age
        self.height = height
        self.name = name


rq = requests
f = foo
h = Human
h = 100

"""
print(requests.__name__)
print(rq.__name__)
print(foo.__name__)
print(f.__name__)
print(Human.__name__)
print(h.__name__)
print(__name__)

print(type(Human))
print(type(h))
print(type(foo))
print(type(f))"""
'''
list = []'''
for method in dir(colorama):
    print(method)
'''
name = "Vlad"
print(hasattr(name, "reverse"))
print(hasattr(name, "index"))
print(getattr(name, "startswith"))
print(getattr(name, "startswith"), None)

print(callable((name)))
print(callable((foo)))'''

class First:
    pass


class Second(First):
    pass
"""
print(issubclass(First, Second))
print(issubclass(Second, First))"""
"""
s = Second()
print(isinstance(s, Second))
print(isinstance(s, First))"""

import  inspect
'''
print(inspect.ismodule(Second))
print(inspect.isclass(Second))
print(inspect.isfunction(Second))'''

signature = inspect.signature(Human)
print(signature)
for param in signature.parameters.values():
    print(param.name, param.default)

