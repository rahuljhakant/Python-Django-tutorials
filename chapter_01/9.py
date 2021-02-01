"""
Generators:
-----------
Generators are like iterators, but are easier than iterators, because they don't use iter() and next()
function.
It works with the yeild statement.

When we call the yeild(), it changes the value and goes back to the loop again.
"""

"""

Late binding:
-------------
It is very simple to create a generator in python.

Just create any function and instead of using return, use yield(), at the time of execution,
that method will be treated as generator.

The difference between both of them is, that return statement terminates the function execution.
The yield() statement calls and stay Idle, and until it get the call again and in the next call,
it executes from there on.
"""


def music_player():
    playlist = range(1, 6)
    for song in playlist:
        print('Playing song number', song)
        yield song


next_song = music_player()
next(next_song)
next(next_song)
next(next_song)
next(next_song)
next(next_song)
