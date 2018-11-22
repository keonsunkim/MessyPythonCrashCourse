"""
Python for statement flows!
"""


for something in 1:
    print(something)
# comment out above to run other for statments!
# We cannot run a for statement with '1' it is simply not iterable!


a = [1, 2, 3, 4, 5]

for num in a:
    print(f'hey the num in a is {num}')

"""
a for statements can anything which can be iterable!
It will sequentially (if there is a sequence) bring out
elements in a iterable group of elements!"""

a = {'hut': 1, 'two': 2, 'three': 3, 'four': 4, 'teemo': 'teemo'}

for dialogue in a:
    print(dialogue)

"""
A dictionary's order is not guaranteed but it is still iterable
since even though without an order we can its elements one by one!
"""

for key, value in a.items():
    print(f'key is {key} and value is {value}')
"""
If there can be two parameters catched, just like cases regarding dictionaries
(has key and value) with the items() method, you can allow the for to catch 
two values by setting two variables!"""

for num in range(5):
    print(f'''{num}'th' num in range(5) is {num}''')
"""
we can also a code block a desired amount of time using the range()
expression! Note that the num starts from 0!"""


for num in range(5):
    print(f'''{num+1}'th' num in range(5) is {num+1}''')
# simply num + 1 for it to start from 1!


a = list()
print(f'a before for statment {a}')
for num in range(5):
    a.append(num + 1)
print(f'a after for statment {a}')

"""
to create a list with incrementing numbers, we could append the numbers
to a list every time a for for statment block is run! """

a = list()
print(f'a before even number creating for statment {a}')
for num in range(10):
    if (num + 1) % 2 == 0:
        a.append(num + 1)
    else:
        pass
print(f'the we created a numbers list with even numbers!! {a}')
# we can combine a if else statment in a for statement!
