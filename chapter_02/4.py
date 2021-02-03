"""
Decorators()

Decorators are a very powerful concept in python.
It is used when we don't want to use the function in a different way but don't want to
change the original function.

So, we create another decorator function and call the main function() from it.
"""


def div(a, b):
    print(a / b)


def decorator_function(func):
    def inner_func(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner_func


dec = decorator_function(div)
dec(4, 2)
