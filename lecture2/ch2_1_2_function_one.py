"""
A function module to show an example for '__main__' argument!
This module is in set with 'ch3_1_3_function_two.py' which contains
a function checker!
"""

# we need an __init__.py file to let python treat this as a package!

import ch3_1_3_function_two


def func_in_one():
    print("func() in the function_one.py")


if __name__ == "__main__":
    print("function_one.p is being run directly")
else:
    print("function_one.p is being imported into another module")
# file two.py

func_in_one()
ch3_1_3_function_two.func_in_two()
