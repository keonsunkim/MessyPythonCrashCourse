"""
Python if else flow
"""

a = True

if a is False:
    print('a is false')
elif a is True:
    print('a is True')
else:
    print('what is a?')

"""
The base structure of a an if else statment is that it checks a
expression on if, then if the expression is True, executes the code
on the if block.
If not, it will check the next expression on elif (if there is one),
or it will run the code block on else:"""

a = 1.2
if a % 2 is 0:
    print('a is an even number')
elif a % 2 is 1:
    print('a is an odd number')
else:
    print('maybe a is not an integer?')

"""
not only checking boolean types, if else statements can check complex
expressions with operations! """

a = 'abc'

if 'b' in a and 'c' in a:
    print('there is both b and c in a!')
elif 'c' or 'a' in a:
    print('there is either c or a in a!')
else:
    print('hmmm')

"""
the expressions in if else statments can also include and, or operators
the expressions with the and or operator will be checked!"""

a = []
if a:
    print('a is not empty!')
elif not a:
    print('a is empty!')
else:
    print('this should not happen!')

"""
one of the points of if else statements is that it can not only check 
Nonetypes, but also whether lists, tuples, dicts are empty or not.
Above follows the PEP8 recommended coding style. Deal with it and get used to it
"""

a = 3
if a is 1:
    print('a is one')
elif a % 2 is 1:
    print('a is an odd number')
elif a is 2:
    print('a is two')
elif a is 3:
    print('a is three')
else:
    pass


"""
Last point! If else statements are checked from top to bottom!
Even when an expression may be true, if an expression above the expression 
was true, then the expression simply will not be checked """
