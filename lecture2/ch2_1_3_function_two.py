"""
A function module to show an example for '__main__' argument!
This module is in set with 'ch3_1_2_function_one.py' which contains
the module to be run!
"""
print('ch3_1_3_function_two.py being imported!')


def func_in_two():
    print("func_in_two in ch3_1_2_function_two.py is called!")

if __name__ == "__main__":
    print("ch3_1_3_function_two.py is being run directly")
else:
    print("ch3_1_3_function_two.py is being imported into another module")
