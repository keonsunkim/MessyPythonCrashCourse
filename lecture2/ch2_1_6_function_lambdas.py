"""
Brief Introduction to Python Lambdas
"""

a = lambda x: x * 2
print(f'the type of the lambda function "a" is {type(a)}')

# we can see that just like other functions, lambda is also classified
# as a function


def list_multiplier(num_list, multiplier):
    multiplied_list = list()
    for num in num_list:
        multiplied_list.append(num * multiplier)
    return multiplied_list

a = [1, 2, 3, 4]
a_times_four = list_multiplier(a, 4)

print(f'all the elements in a multiplied by 4 is {a_times_four}')

"""
Suppose you want all the elements multiplied by 4.
The method avove can be a bit troublesome"""


a_times_four2 = list(map(lambda x: x * 4, a))
print(f'a * 4 through lambda function is {a_times_four2}')

# We can easily acheive the result above with a simple
# lambda function

print(f'2 + 4 is {(lambda x, y: x + y)(2, 4)}')

"""
Adding two numbers with lambda
So what is lambda anyways? Lambda is an anonymous function
used to simplify code and sometimes make it easier to read"""


def odd_nums(num_list):
    odd_nums = list()
    for num in num_list:
        if num % 2 == 1:
            odd_nums.append(num)
    return odd_nums

a = [1, 2, 3, 4]
a_odd_nums = odd_nums(a)

print(f'the odd numbers in list a is {a_odd_nums}')

odd_nums2 = list(filter(lambda x: x % 2 == 1, a))
print(f'odd numbers found through lambda is {odd_nums2}')

"""
Lambdas come especially handy with filter and map functions which
applies a certain function over all the elements in a python list.
"""
