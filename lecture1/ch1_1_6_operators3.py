"""
The difference between: "==" and "is" operators
This can be a bit confusing!! 
Note that "==" operator distinguishes whether
two operands have the same value and that 
"is" operator distinguishes whether two operands
refer to the same object!
"""

a = [1, 2, 3]
b = [1, 2, 3]
# we have two lists that have the same value!!

print(f'"a is b" is {a is b}')
print(f'"a == b" is {a == b}')
# seems like the same, but are different!

print(f'id of a is {id(a)}')
print(f'id of elements in list a: \n\
	a[0] is {id(a[0])} \n\
	a[1] is {id(a[1])} \n\
	a[2] is {id(a[2])} ')

print(f'id of b is {id(b)}')
print(f'id of elements in list b: \n\
	b[0] is {id(a[0])} \n\
	b[1] is {id(a[1])} \n\
	b[2] is {id(a[2])} ')

"""
The id(memory location) of the list are different while
the elements of the list are the same
"""

a = b
print('now a = b')
print(f'"a is b" is {a is b}')
print(f'"a == b" is {a == b}')
print(f'id of a is {id(a)}')
print(f'id of b is {id(b)}')
# b referes to a variable then everything becomes the same


a = 1
b = 1
print('now a = 1, b = 1')
print(f'"a is b" is {a is b}')
print(f'"a == b" is {a == b}')
# reminder for last class!
