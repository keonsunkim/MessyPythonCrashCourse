"""
Declaring variables are easy in python. 
You do not need to explicitly declare types unlike languages 
like C, Java, typescript...
Python will set types for you. 
This works because python variables are all objects! 
"""

var1 = 'a'    # this is a 'str'
var2 = 2      # this is a 'int'
var3 = 2.3    # this is a 'float'
var4 = 'abc'  # this is a 'str'
var5 = [1, 2, 'a', 'ad']   # this is a 'list'
var6 = (1, 2, 'b', 'be')   # this is a 'tuple'
var7 = {'key': 'value', 'a': 1}  # this is a 'dict'


def print_var_and_type(var):
    # you can print out variables with the builtin
    # print() function
    # f'strings' will be explained in later modules
    return print(f'{var}{var} is {type(var)}')

# let's print out the variable values and types
print_var_and_type(var1)
print_var_and_type(var2)
print_var_and_type(var3)
print_var_and_type(var4)
print_var_and_type(var5)
print_var_and_type(var6)
print_var_and_type(var7)
