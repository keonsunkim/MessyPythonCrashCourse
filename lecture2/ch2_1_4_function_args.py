"""
*args, parameters in Python functions
"""


def addition_for_two_num(first_num, second_num):
    result_num = first_num + second_num
    return result_num

two_plus_four = addition_for_two_num(2, 4)
print(f'two_plus_four is {two_plus_four}')

"""
Our addition function from last time.
But what if we want to do addition operations on a
set of numbers which cannot be known before runtime?"""


def addition_for_multiple_num(first_num, second_num, third_num=0,
                              fourth_num=0, fifth_num=0,
                              sixth_num=0,
                              ):

    addition_val = first_num + second_num + third_num + fourth_num \
        + fifth_num + sixth_num
    return addition_val

addition = addition_for_multiple_num(3, 4, 5, 6, 7)
print(f'adding multiple numbers 3, 4, 5, 6, 7, is {addition}')
"""
one way we could achieve this would be by allowing the user
to ommit parameters. However we can see that things will get extremely
tedious once we try to recieve multiple numbers."""


def addition_for_nums_in_list(num_list=[]):
    base_num = 0
    for num in num_list:
        base_num += num
    return base_num

addition = addition_for_nums_in_list([3, 4, 5, 6, 7])
print(f'adding multiple numbers in list = [3, 4, 5, 6, 7] is {addition}')

"""
we can recieve values in list form and just iterate through it. this saves
ourselves from doing something very tedious. But what if we have much more to
recieve?"""


def addition_for_num(*args):
    base_num = 0
    for num in args:
        base_num += num
    return base_num

addition = addition_for_num(1, 2, 3, 4, 5, 6)
print(f'adding multiple numbers 1, 2, 3, 4, 5, 6 is {addition}')

"""
See that we can pass parameters without any positional arguments,
through the *args.
What happens here is that *args captures all the values without any
positional arguments and puts it in the args list"""


def addition_for_num(starting_num, *args):
    print(f'starting_num is {starting_num}')
    print(f'args list is {args}')
    for num in args:
        starting_num += num
    return starting_num

addition = addition_for_num(1, 2, 3, 4, 5, 6)
print(f'adding multiple numbers 1, 2, 3, 4, 5, 6 is {addition}')

"""
The first parameter 1 is set as the starting_num due to its positional
argument. All the other values which does not have a positional argument
is captured by the *args"""


def args_demonstrate(args1, args2, args3):
    print(args1)
    print(args2)
    print(args3)

args = ['hey', 'you', 'hey!']
args_demonstrate(*args)
"""
The '*' character causes the list to be unpacked in the parameter argument field.
Each elements in the list args is unpacked to provide each positional arguments
args1, args2, args3 its corresponding value sequentially"""


def args_demonstrate2(args1, args2, args3, *args):
    print(f'args1 is {args1}')
    print(f'args2 is {args2}')
    print(f'args3 is {args3}')
    print(f'args is {args}')

args = ['hey', 'you', 'hey!', 'extra1', 'extra2']
args_demonstrate2(*args)
# Another example how *args may be used with the positional arguments.


def args_demonstrate3(args1, args2, args3, *args):
    print(f'args1 is {args1}')
    print(f'args2 is {args2}')
    print(f'args3 is {args3}')

args = ['hey', 'you', 'hey!', 'extra1', 'extra2']
args_demonstrate2(*args)
# we can even let the extra parameters to be passed. Just don't call them!
