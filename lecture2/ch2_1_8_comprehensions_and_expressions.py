"""
Python List Comprehensions and Generator Expressions
"""


def create_even_incre_sequence(num):
    incre_list = list()
    for i in range(num):
        if i % 2 == 0:
            incre_list.append(i + 2)
    return incre_list

even_num_to_ten = create_even_incre_sequence(10)
print(even_num_to_ten)

"""
Creating a list sequence which needs to be referencing from another
sequence can be troublesome. See how much work is needed just
to create a relatively simple list"""

incre_num_list = [i + 1 for i in range(10)]
print(incre_num_list)

"""
Creating a sequence can be simplified by using a list comprehension.
we are getting all the variable 'i' given by the "for i in range(10)"
statement and appending it to a list"""


even_num_incre = [i + 2 for i in range(10) if i % 2 == 0]
print(even_num_incre)
# We can even set simple logic to a list comprehension!

# Lets create a list which looks like the following
# [1, '-', 1, '-', 1, '-'...]

target_list = [1 if i % 2 == 0 else '-' for i in range(10)]
print(target_list)

# Play around to get used to it!


incre_num_set = {i + 1 for i in range(10)}
print(incre_num_set, type(incre_num_set))
# we can also create sets just by setting the brackets differently

"""
Identitcal logic used in list comprehensions can be used to create 
generators easily. We just set the brackets as '()'"""


def give_even_incre_sequence(num):
    for i in range(num):
        if i % 2 == 0:
            yield i + 2

for even_num in give_even_incre_sequence(10):
    print(even_num)

# remember what we learned on the previous module

incre_even_num_gen = (i + 2 for i in range(10) if i % 2 == 0)

print(type(incre_even_num_gen))
for even_num in incre_even_num_gen:
    print(even_num)

# See how easily a generator can be created!
# They are called Generator Expressions


target_list_gen = (1 if i % 2 == 0 else '-' for i in range(10))

for target_element in target_list_gen:
    print(target_element)

"""
The rules on creating generators are identical to the rules applied
in creating list comprehensions. 
Only the difference in brackets cause a expression to be a 
list comprehension or generator expression"""
