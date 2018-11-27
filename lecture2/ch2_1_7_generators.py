"""
Python Generators!
"""


def create_even_incre_sequence(num):
    incre_list = list()
    for i in range(10):
        print(f'The for statement ran {i+1} times')
        if i % 2 == 0:
            incre_list.append(i + 2)
    return incre_list

even_num_to_ten = create_even_incre_sequence(10)

for num in even_num_to_ten:
    print(num)

"""
Suppose we want to want to print incrementing even numbers.
We could achieve it through a simple "for num in range(10)",
statement but we created a function since we wanted to repeat
the numbers with different maximums.
Then we have to create a function which creates  a list of even
numbers in incrementing order, recieve a list for a specific
maximum, iterate it over and print it.
Can it be simpler??"""


def incrementing_generator(num):
    for i in range(num):
        print(f'The for statement ran {i+1} times')
        yield i

for num in incrementing_generator(10):
    print(num)


"""
We created a generator object which gives out a sequence if incrementing
numbers one by one. We can confirm that the for statement is not completed
when it is called, rather the block inside the for statement is run
everytime the for statement calling the generator 
('for num in incrementing_generator(10)' <- this for statement!!!).
"""

# When would you want to create a generator??


def create_even_incre_sequence(num):
    incre_list = list()
    for i in range(num):
        if i % 2 == 0:
            incre_list.append(i + 2)
    return incre_list

even_num_to_million = create_even_incre_sequence(1000000)

for num in even_num_to_ten:
    print(num)

# the code above will make your pc fan go wild! Comment them out
"""
Imagine a case we need to repeat a certain task or do some work
on an extremely big object of sequences. It will eat up your memory 
really quickly like the simple code above which prints from 1 to a million
"""


def give_even_incre_sequence(num):
    for i in range(num):
        if i % 2 == 0:
            yield i + 2

for num in give_even_incre_sequence(10000000):
    print(num)

# A generator is a quick fix to the problem above
