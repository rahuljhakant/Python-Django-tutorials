"""
List comprehension:
-------------------
It is a powerful concept of the Python, In list comprehension we can write multiple statements into a single line.
It is faster than for loop and increase the performance of the code.
"""

"""
To print the value from 1 to 10
"""
listComprehension = [value for value in range(1, 11)]
print(listComprehension)

"""
print list which has only even values till 20
"""

listComprehension1 = [value for value in range(1, 20) if value % 2 == 0]
print(listComprehension1)