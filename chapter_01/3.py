"""

Tuple:
To understand tuple we have should know about two words:
1. Mutable : which can be changed.
2. Immutable : which cannot be changed.

"""

a = (1, 2, 3, 4)
print(a)
a.appednd(6)  # This will give an error "AttributeError: 'tuple' object has no attribute 'append'"

"""
or
"""

b = 1, 2, 3, 4
print(b)
# b.append(5) This will give an error "AttributeError: 'tuple' object has no attribute 'append'"

