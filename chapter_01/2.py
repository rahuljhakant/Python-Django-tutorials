# List

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 20]
b = ['a', 'b', 'c', 'd', 'e']

print(min(a))  # smallest value
print(max(a))  # max value

print(a.count(20))  # count of elements

a.append(21)  # add an item to the list
print(a)

a.extend(b)
print(a)  # connect two list

print(len(a))  # length of the list

a.reverse()
print(a)  # reverse list

print(a.index(7))  # index location of elements

a.insert(1, "inserted")
print(a)  # add new element into a particular location

print(a.pop(1))  # remove element
print(a)

a.remove(3)
print(a)  # remove specific element

c = [5, 2, 9, 8, 4, 2, 5, 7]
c.sort()
print(c)  # sort element in sequence

aa = ("a", "b", "c", "d", "e", "f", "g", "h")
xa = slice(2)
print(aa[xa])  # slice function
