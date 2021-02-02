"""
init()
init method is called automatically and suddenly after the declaration of the class instance.

when a programmer creates the instance of the class,that internally calls the init method.

It is a coding convention that init() method is defined with parameter and
that first parameter itself.
"""

"""
The following code block is used to explain the _init_ method and self keyword.
"""


class Cal(object):
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def sum(self):
        print(self.val1 + self.val2)

    def sub(self):
        print(self.val1 - self.val2)

    def prod(self):
        print(self.val1 * self.val2)


c1 = Cal(10, 20)
c1.sum()
c1.sub()
c1.prod()
