import sys


"""
Python try except flows!
"""

# lets say we have some case like below!
a = [1, 2, 3, 4]

if a[4]:
    print(f'the index 4 of list a is {a[4]}!!')
else:
    print(f'list a does not have index 4!')

# comment out above to run codes below
"""
unlike what we wanted, the code above will throw an error
it has an index error"""

try:
    print(f'the index of 4 of list a is {a[4]}!')
except:
    print(f'list a does not have index 4!')

# by utilizing a try except statement, we can achieve what we originally
# wanted!

try:
    print(f'the index of 4 of list a is {a[4]}')
except Exception as e:
    print(e)

# be catching the exception in the except clause, we can even print
# what kind of error we are seeing!

try:
    print(f'the index of 4 of list a is {a[4]}')
except IndexError:
    print(f'list a does not have index 4!')
except Exception as e:
    raise
"""
However it is not good practice to allow your code to be lenient on all types
of errors. It is best to control what type of errors you will allow.
We know that there is an index error prone clause, and we want to allow an
IndexError but we don't want any other errors to be passed.
Then we specifically allow only Index errors and allow python to raise all the other
errors as errors!"""

b = 4
try:
    print(f'b + "abc" is {b + "abc"}')
except IndexError:
    print(f'list a does not have index 4!')
except Exception as e:
    raise

# comment out the code right above to run other codes
# code above only allows index errors and will raise errors and stop code execution!
# above is a better way since we control what types of errors will be raised!


b = 4
try:
    print(f'b + "abc" is {b + 4}')
    if b > 3:
        raise ValueError("b should be bigger than 4")
except:
    raise

"""
Finally, you can also raise your own errors. Although it is a more complex and 
advanced case, It can be a good way to track your code.
You could also create your error class! But not for now """
