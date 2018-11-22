import time

"""
Python while statment and flow
"""

while True:
    print('This will go on forever!!!!!')
    print('Control + C to quit!')
    time.sleep(1)

# comment out the while above to run other codes
"""
While statements will repeat the code block inside the while until
a the expression that constitutes the while statement is satisfied!
The code above wil run forever! """

num = 1
while num < 10:
    print(num)
    num += 1

# In the case above, the code block will run 9 times! see what happens!

num = 1
while True:
    print(num)
    num += 1
    if num > 9:
        break
# we could also set an if -> break statement to stop a while statement!


yes_or_no = 'yes'
while True:
    yes_or_no = str(input("Keep going???? : "))
    yes_or_no.lower()
    if yes_or_no != 'yes' and yes_or_no != 'no':
        print("Not a valid answer we shall ask again")
    else:
        if yes_or_no == 'yes':
            print('lets go!')
            pass
        else:
            print('stop this madness')
            break

"""
while statements are especially useful for cases when we cannot predetermine
the breaking point. In the code above when to stop the repetition is solely dependent
on the end user's decision!"""

# note that if we change the == to the 'is' operand things will break! This is because
# two strings are saved in different memory points!

yes_or_no = 'yes'

while yes_or_no == 'yes':
    yes_or_no = str(input("Keep going???? : "))
    yes_or_no.lower()
    if yes_or_no != 'yes' and yes_or_no != 'no':
        print("Not a valid answer we shall ask again")
        yes_or_no = 'yes'

# we can acheive the same flow of the previous code with the code above!
