"""
Python Iterators
"""

a = [1, 2, 3, 4]

print(f'our {type(a)} "a" hass attribute __iter__',
      f': {hasattr(a, "__iter__")}')

b = 'abcdef'
print(f'our {type(b)} "b" hass attribute __iter__',
      f': {hasattr(b, "__iter__")}')

c = (1, 2, 3, 4)
print(f'our {type(c)} "c" hass attribute __iter__',
      f': {hasattr(c, "__iter__")}')

d = {'a': 1, 'b': 2, 'c': 4}
print(f'our {type(d)} "d" hass attribute __iter__',
      f': {hasattr(d, "__iter__")}')

"""
A iteratable in Python is any object which has an '__iter__'
method inside it. As we can see all of the types checked above
has a '__iter__' method within them.
By applying a iter(), which is a method makes the iterable into an
iterator, we can transform them into an iterator.
"""

iterator_a = iter(a)
print(f'bring out next element from iterator_a = {next(iterator_a)}')
print(f'bring out next element from iterator_a = {next(iterator_a)}')
print(f'bring out next element from iterator_a = {next(iterator_a)}')
print(f'bring out next element from iterator_a = {next(iterator_a)}')
# print(f'bring out next element from iterator_a : {next(iterator_a)}')
# uncomment the code above to see the stop iteration error

"""
When turned into an iterator, we can bring out the elements in the
list 'a' one by one until it raises a StopIteration. This means we can
bring out the elements of a list until we deplete it."""

iterator_d = iter(d)
print(f'bring out next element from iterator_d = {next(iterator_d)}')
print(f'bring out next element from iterator_d = {next(iterator_d)}')
print(f'bring out next element from iterator_d = {next(iterator_d)}')

# Even dictionaries have an __iter__ method!

print(f'The type of the iterator_a is {type(iterator_a)}')
print(f'The type of the iterator_d is {type(iterator_d)}')

"""
See how the list and dict have changed respectively to a
list_iterator and a dict_iterator. """


def func_style_generator():
    for num in range(10):
        yield num

print(f'The type of the func_style_generator() is {type(func_style_generator())}')

print(f'The func_style_generator() has attribute __iter__,',
      f'{hasattr(func_style_generator(), "__iter__")}')

g = func_style_generator()

print(f'bring out next element from iterator_d = {next(g)}')
print(f'bring out next element from iterator_d = {next(g)}')
print(f'bring out next element from iterator_d = {next(g)}')

"""
A generator also has a method iter. In fact, generators are already
iterators since they can be called through the next() method.
Generators unlike other iterable objects (such as lists, dicts, strings...)
does not hold any fixed values. Remember that! It only yields a sequence
of values when called.
"""

"""
Summing up...
Iterables are anything which is or can be an iterator.
Iterators are anything can yield values in order when called. 
Thus Lists, Dicts, Strings
are Iterables since they can become an iterator through the iter() method.
However they are not iterators since their elements cannot be called separately
in a orderly fashion. The elements are still contained in a 'container'.
On the other hand, generators are already iterators. They are not contained.
In fact, they do not hold any values. They merely yield values in an order 
every time they are called. Also, since they already are iterators, they are
iterables. They can be iterated!"""
