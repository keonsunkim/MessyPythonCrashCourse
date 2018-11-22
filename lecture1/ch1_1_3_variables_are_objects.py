"""
Understand how python data items are all objects
"""

# 1 = 'abc'  # this will throw out an error!
# class = 'abc'  # this wil also throw an error!
"""
there are 33 names that cannot become names for variables
they are called reserved keywords! 
comment the code aboveout to run other code
"""

var1 = 1
print(id(var1))
print("Changing value of var1 to 2")
var1 = 2
print(id(var1))
"""
the id of a variable is changing because the variable object
is referencing different values in different locations in memory
"""

var2 = 2
print(id(var1), id(var2))
"""
this becomes more clear when you see how to variables can share 
the same id
"""

var1 = 1
print("Changing value of var1 back to 1")
print(id(var1), id(var2))

"""
The id of the variable changes again!
"""
