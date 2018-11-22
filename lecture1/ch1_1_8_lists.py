"""
Python lists and list methods
"""

a = [1, 2, 3, 4, 'a', 'b', 'c', 'd', 'xyz', [1, 2, 3], 'end']

print(f'a[0] is "{a[0]}", and a[-11] is "{a[-11]}"')
print(f'a[5:] is "{a[5:]}", and a[-6:] is "{a[-6:]}"')
print(f'a[1:11] is "{a[1:11]}", and a[-15:-5] is "{a[-15:-5]}"')
# just like strings, you can access list values through indexes

a[0] = 9

print(f'now a is {a}')
# unlike strings, lists are mutables. You can change list values through
# indexes!


# list methods: .count() .remove() .append() .extend()
# .sort() .pop() .filter() .clear()

a = [1, 2, 3]

"""
Before even beginning, we must be aware that some methods do not return anything!
They will apply the transformation to the list itself! 
"""

a_sorted_method_applied = a.sort()
print(f'the return value of .sort() method is {a_sorted_method_applied}!!')
# example!

num_of_one = a.count(1)
print(f'the number of 1 in a is {num_of_one}')
# we can count the number of certain elements in a list using count()

a.remove(1)
print(f'the list a is {a} after we remove 1 from it')
# we can remove fist matching value!

a.append(2)
print(f'the list a is now {a} when we append 2')

a.extend([4, 5, 6])
print(f' the list has been extended to {a} after we extended \
	"[1, 2, 3] to a')

a = [1, 2, 3]
# re define a to [1, 2, 3] to see the difference between the extend
# and append method
a.append([4, 5, 6])
print(f'when we append "[1, 2, 3]" to list a, a will be modified to {a}')

a = [1, 2, 3]
# re define a to [1, 2, 3] to see the difference between the extend
# and append method
a.extend([4, 5, 6])
print(f'when we extend "[1, 2, 3]" to list a, a will be modified to {a}')

a1 = [1, 2, 3]
a2 = [1, 2, 3]
# declare two lists with identical values for demonstration purposes
print(f'appended a = {a1.append([1, 2, 3])}, \
	    extended a = {a2.append([1, 2, 3])}')

messy_a = [2, 5, 3, 7, 1, 9]
# define unsorted list to see what sorted() and .sort() does


def sorter(some_list):
    some_list.sort()
    return some_list

print(f'unordered list {messy_a} will turn to {sorter(messy_a)}, when\
	using the sorted() function')

messy_a = [2, 5, 3, 7, 1, 9]

print(f'unordered list {messy_a} will turn to \
	{(lambda x: sorted(x))(messy_a)}, when using the sorted() function')
# we will later cover lambda functions!


a = [1, 2, 5, 3]
pop_value = a.pop(1)
# pop will remove the list element by its index and return the removed value!
print(f'when we execute "pop_value = a.pop(1)" then pop_value = {pop_value}, \
	a = {a}')


a = [1, 2, 3]
b = a.copy()
# a copy method creates a copy of a list and returns it!

print(f'when b = a.copy(), then a = {a}, b = {b}')
print(f'but take in note that a == b -> {a == b}, but a is b -> {a is b}')
# a == b is true and a is b is false due to the reason how python checks
# the conditions! see how variable declarations work!!


def is_even_num(num):
    if num > 0:
        return True
    else:
        return False

# b = filter(is_even_num, a)
b = filter(lambda x: x > 0, a)
for c in b:
    print(c)
a = [2, 1, 3]
a.sort()
print(a)
