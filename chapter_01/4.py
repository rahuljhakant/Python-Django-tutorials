"""
Dictionaries : It stores values in key, Value pairs.
where Keys are immutable and values are mutable.

dict = { key:values }

empty dictionary:
dict = {}
"""

"""
Referencing the dictionary object:
---------------------------------
dict2 = dict1
Here changes in one object reflect the changes in another object.
"""

abc = {1: 'one', 2: 'two', 3: 'three', 4: 'Four'}
xyz = {}

xyz = abc
print(xyz)

"""
dict2 = dict1.copy()
Here dictionary 2 copied all the objects of  dict1 so if we change the object of dict1,
it will not reflect in dict1
"""

'''
Dictionary built in function:
'''
print(abc.items())
print(abc.keys())
print(abc.values())
print(abc.get(2))

'''
fromkeys()
It creates a new dict from the given sequence and value of element from the user
'''
l1 = [1, 2, 3, 4, 5, 6, 7, 8]

dict1 = {}
dict2 = dict1.fromkeys(l1, 'default value')
print(dict2)

'''
clear() removes all the items from the dictionary
'''

# dict2.clear()
# print(dict2)

'''
pop(), It removes key and return value, if the key is not present then it return the given default value.
'''
print('test')
print(dict2.pop(8, 'Not found'))
print(dict2)

'''
update : It updates key and can add new (key, value) tp the dictionary.
'''

dic1 = {1: 'aaa', 2: 'bbb', 3: 'ccc'}
dic2 = {4: 'ddd'}

dic1.update(dic2)
print(dic1)

'''
popitem() It removes the last element from the dictionary.
'''

result = dic1.popitem()
print(result)

'''
setdefault() : It returns the value of a key of the key is already exists.
If not then it inserts key with a given value, then it returns the given default value
'''
print(dic1.setdefault(6, "Value not present"))

'''
performing loop on the dictionary
an example of a vending machine which implements a dictionary
'''


def vending():
    vending_machine = {1: 'coffee', 2: 'Tea', 3: 'Juice', 4: 'black tea', 5: 'latte'}
    for i in vending_machine.items():
        print('Please select one value from the machine  :')
        user_input = input()
        if int(user_input) in list(vending_machine.keys()):
            print(vending_machine.get(int(user_input)))
            exit()
        else:
            print('Invalid value, please select again.')
            vending()


vending()
