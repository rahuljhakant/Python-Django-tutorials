"""
Set is a collection of unordered and unique elements.
set1 = {}
set2 = ()

"""

set1 = {1, 2, 3, 4}
print(type(set1))

# best way to define a empty set is:
set2 = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
print(type(set2))

# type cast a list to a set
lis1 = [1, 2, 3, 4, 5]
print(type(set(lis1)))

"""
creating an empty set is tricky because
"""
empty_set = {}
"""
can be treated as a dictionary so,
"""
set3 = set()
print(type(set3))

"""
Types of sets,
1. Frozen sets
2. sets

sets : mutable
frozen sets : immutable sets
"""

"""
Built in methods for sets:
"""

newSet = frozenset(set1)
print(type(newSet))

print(newSet)

allSet = set(set2)
print(type(allSet))
print(allSet)

"""
Built-in methods for sets
"""
allSet.add(11)
print(allSet)
alphaSet = {99}
# exception is frozen set
print(allSet.union(alphaSet))

aaa = {1, 2, 3, 4, 5, 6}
print(allSet.difference(aaa))

allSet = aaa.copy()
print(allSet)

print(aaa.clear())

allSet.remove(6)
print(allSet)

print(allSet.intersection(set1))

"""
isdisjoint():
It will check into both sets and if it is not found in any set then it returns true value else false
"""

dis1 = {1, 2, 3, 4}
dis2 = {5, 6, 7, 8}

print(dis1.isdisjoint(dis2))

'''
issubset()
It will check if set1 is a part of set2, if yes then it will return true else false.
'''

if dis1.issubset(allSet):
    print("Is a part of")
else:
    print("Is not a part of")


'''
pop()
It removes an arbitrary element from the set, means it will randomly remove 
any element from the list.
'''
print(allSet)
print(allSet.pop())
print(allSet)