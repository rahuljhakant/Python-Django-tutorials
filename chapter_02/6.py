"""
Inheritance:
-----------
Inheritance means code usability, it means write the code once and use it multiple times.

types of inheritance in python:
-----------------------------
single
multiple
multilevel
"""

"""
Single inheritance
"""


class Mouse:

    def __init__(self, mouse_quantity):
        self.mouse_quantity = mouse_quantity

    def product_availability(self):
        print("Mouse quantity from mouse class is: ", self.mouse_quantity)


class ProductStock(Mouse):

    def __init__(self, mouse_quantity, keyboard_quantity, display_quantity):
        self.mouse_quantity = mouse_quantity
        self.keyboard_quantity = keyboard_quantity
        self.display_quantity = display_quantity
        Mouse.__init__(self, mouse_quantity)

    def product_stock_details(self):
        print(self.mouse_quantity)
        print(self.keyboard_quantity)
        print(self.display_quantity)


p = ProductStock(11, 22, 222)
p.product_availability()
p.product_stock_details()
