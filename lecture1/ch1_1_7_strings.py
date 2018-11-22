"""
Python strings and string methods
"""

a = "This is a string"

print(f'a[0] is "{a[0]}", and a[-16] is "{a[-16]}"')
print(f'a[10:] is "{a[10:]}", and a[-6:] is "{a[-6:]}"')
print(f'a[1:11] is "{a[1:11]}", and a[-15:-5] is "{a[-15:-5]}"')
# you can access strings through indexes

# a[1] = '1' # this will spit an error

a = 'abc'
# assign variable a with a string value

print(f'type of "a" is {type(a)}')

# string methods  .replace() .strip() .lower() .upper() .split() len()

print(f'a is {a}')
# check the value before applying string methods

a = a.upper()
print(f'a.upper() will change a to {a}')
# the .upper() method changes all the elements into capital case

a = a.lower()
print(f'a.lower() will change a to {a}')
# the .lower() method changes all the elements into lower case

len_a = len(a)
print(f'len() will return the length of a string which is {len_a}')
# the len() method returns the length of a string

a = a.replace("a", "d")
print(f'a.replace("a", "i") will change a to {a}')
# the replace() will locate every values which match the first parameter
# and replace with the second parameter in the parenthesis

a = a.split('b')
print(f'a.split("b") will return {a}')
# the split method splits the as the given parameter as a reference point
# and returns a list containing strings
