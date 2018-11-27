"""
**kwargs parameters in Python functions
"""


def print_greetings(*args):
    for arg in args:
        if arg.startswith('hey'):
            print(arg)
        elif arg.startswith('hel'):
            print(arg)
        elif arg.startswith('goodm'):
            print(arg)
        else:
            pass


print_greetings('hey', 'you', 'goodmoring', 'hello!', 'extra1', 'extra2')

# there might be a case we might want to identify and use certain
# values in the arguments


def kwarg_demonstration(**kwargs):
    print(kwargs)

kwarg_demonstration(greeting=['goodmoring', 'hello', 'hey'],
                    person='you', extra=['extra1, extra2'])

"""
We can give attributes (specifically keys) to the parameters
we are passing. We can capture the keys and its corresponding
values through the **kwargs argument"""


def only_greeting(**kwargs):
    greeting = kwargs.get('greeting')
    for word in greeting:
        print(f'word in greeting keys is {word}')

only_greeting(greeting=['goodmoring', 'hello', 'hey'],
              person='you', extra=['extra1, extra2'])

"""
We can recieve extra parameters and use cherrypick the 
arguments we want."""


# def only_greeting_try(*args):
#     print(args)

# only_greeting_try(greeting=['goodmoring', 'hello', 'hey'],
#                   person='you', extra=['extra1, extra2'])

# comment out above to run other codes
# if we try to capture extra keyword arguments through the
# args parameter, then an error will be raised

def args_kwargs_mix_use(*args, **kwargs):
    print(f'args is {args}')
    print(f'kwargs is {kwargs}')

args_kwargs_mix_use(1, 2, 3, 4, 5, greeting=['goodmoring', 'hello', 'hey'],
                    person='you', extra=['extra1, extra2'])

"""
We can capture both extra positional and extra keyword arguments by
explicilty stating *args, **kwargs in our function parameters."""
