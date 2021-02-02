"""
Major pillars of OOPS in python:
> Object
> Class
> Inheritance
> Encapsulation
> Polymorphism
> Abstraction
"""

"""
Object()
"""


class Aircraft:
    print("Welcome to aircraft object")


aircraft_object = Aircraft()

# assigning new values to the class through class object
aircraft_object.c1 = 20
print(aircraft_object.c1)

"""
Any variable that is defined within a class is called a class variable, such
variable can be called outside of the class with the help of the class object.
"""


"""
Self Keyword
------------

self keyword is used to define the method and attribute of the class.
It should be the first parameter.
"""


