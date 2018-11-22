"""
Python switch style flow!
"""

a = 4


def num_to_str(num):
    num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    return num_dict[num]

num_in_str = num_to_str(a)
print(f'a in string is {num_in_str}')

# by checking a given value in a dictionary, we can do what is equivalent
# to the following!

if a is 1:
    print('a in string is one')
elif a is 2:
    print('a in string is two')
elif a is 3:
    print('a in string is three')
elif a is 4:
    print('a in string is four')

# a if, elif, else may be sufficient enough for many cases! But who knows
# if you want to map something really really big. Then a dictionary mapping
# can come in very handy!
