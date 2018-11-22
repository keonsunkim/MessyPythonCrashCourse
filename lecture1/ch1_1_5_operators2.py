"""
Now we look at different types of operators other than the
Arithmetic Operators
"""

a = 1
b = a
# we can declare a variable to be a variable

print(f'a is {a}, b is {b}')

a += 1
print(f'a +=1 is {a}')
# we can do compound declarations

print(f'a is {a}')
a *= 2
print(f'a *= is {a}')
# we can many different kinds of compound declarations

a = True
b = True
# we reassign boolean type values to make life easier

c = a and b
print(f'a and b is {c}, when a = {a} b = {b}')

c = a or b
print(f'a or b is {c}, when a = {a} b = {b}')

# however... when we change a and b to be conflicting
a = True
b = False

c = a and b
print(f'a and b is {c}, when a = {a} b = {b}')

c = a or b
print(f'a or b is {c}, when a = {a} b = {b}')

if a:
    c = True
else:
    c = False
print(f'"if a"is {c}, when a is {a}')

a = None  # False can be the same
if a:
    c = True
else:
    c = False
print(f'"if a"is {c}, when a is {a}')
# the is operator can be a bit tricky
# when None or False, then is False

a = 1
b = 1
# reassign values

c = a is b
print(f'"a is b" is {c}, when a is {a} b is {b}')

c = a is not b
print(f'"a is not b" is {c}, when a is {a} b is {b}')

a = 1
b = [1, 2]
# reassign values to do membership operators

c = a in b
print(f'"a in b" is {c}, when a is {a} b is {b}')

c = a not in b
print(f'"a not in b" is {c}, when a is {a} b is {b}')
