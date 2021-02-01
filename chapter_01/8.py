"""
Iterators:
A set of function which executes repeatedly using either a recursive function call or a loop
is called a iterator.

Iterator element or object returns one element at a time.

In technical terms, python iterator objects always implements with two methods
> iter()
> next(),

sequentially called iterator protocol.
"""

iter_var = iter(range(1, 6))
print(next(iter_var))
print(next(iter_var))
print(next(iter_var))
print(next(iter_var))
print(next(iter_var))

"""
iter() is for defining the elements sequence/range and next() if for calling the next element.
If we call next() and there is no element available then it will given a stop iteration error.
"""

"""
It is in sequence but does nit print the another element until we call the next method,
that is the difference between the iterator and a for loop.
"""

"""
The basic difference between for loop and iterator is that, for loop executes without interruption,
until its all element ends, but iteration start the execute and it holds the next element until next()
method is called.
"""