"""
Python functions 1-1!
"""


def our_first_func():
    print('our first function!')
    print('has been called!')
    print('congratulations!')
    return None

"""
We declare a function by first stating 'def' at the beginning.
Then we set our function name 'our_first_func' then end it with
a bracket '()', The consistuents of the bracket determine what
parameters (variables which our function will recieve to do
certain logic) the funciton will recieve. The bracket must be 
followed by a ':' colon. 
Then we indent to distinguish the following codeblock as a 
logic distinct to the function. 
After we set the logic, the function ends(optionally in python) 
with a return statement which allows the function to return
a certain variable"""

our_first_func()
print('*' * 20)
our_first_func()

# we can call our declared function by calling its name and brackets
# note that we can recreate the logic just by calling the function!


def addition_for_two_num(first_num, second_num):
    result_num = first_num + second_num
    return result_num

two_plus_four = addition_for_two_num(2, 4)
print(f'two_plus_four is {two_plus_four}')

"""
we can apply logic to the parameters by setting some logic inside
the function. And we recieve the outcome of the logic logic through 
the return statment"""


def create_incrementing_list(up_to):
    incre_list = list()
    for num in range(up_to):
        incre_list.append(num + 1)
    return incre_list

list_up_to_ten = create_incrementing_list(10)
print(f'create_incrementing_list() has returned {list_up_to_ten}')


a = 3
b = 5
# declare variables to check!


def side_effect_check(a, b):
    print(f'a before change applied is {a}')
    print(f'b before change applied is {b}')
    a = 6
    b = 9
    print(f'a after change applied is {a}')
    print(f'b after change applied is {b}')
    return None

side_effect_check(a, b)

print(f'a outside of function even though transformation occured '
      f'inside the function is {a}')
print(f'b outside of function even though transformation occured '
      f'inside the function is {b}')
