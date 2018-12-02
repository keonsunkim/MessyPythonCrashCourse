"""
Python Basic Multiple Inheritance.
An Examplery case how dirty our __init__ can become.
"""

"""
Multiple inheritances allow us to
create classes which has features of multiple different classes. 

Our example below, a Employee class uses features of the Person,
and Animal class with its own distinct extension.
"""


class Person(object):

    def __init__(self, name, age, gender, money):
        print('person class init')
        super(Person, self).__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.money = money

    def tell_name(self, name):
        print(f'my name is {name}')


class Animal(object):

    def __init__(self, name, age, gender, money, alive, heartbeat):
        print('animal class init')
        super(Animal, self).__init__(name, age, gender, money)
        self.alive = alive
        self.heartbeat = heartbeat


class Employee(Animal, Person):

    def __init__(self, position, name, age, gender, money, alive, heartbeat):
        super(Employee, self).__init__(
            name, age, gender, money, alive, heartbeat)
        self.position = position

    def tell_position(self):
        print(f'my am only a {self.position}')

    def tell_name(self, first_name, last_name):
        name = last_name + first_name
        super(Employee, self).tell_name(name)


employee1 = Employee('student', 'BSR', '25', 'M', 999999999, True, 90)
print(f'employee position is {employee1.position}')
print(f'employee name is {employee1.name}')
print(f'employee age is {employee1.age}')
print(f'employee heartbeat is {employee1.heartbeat}')

"""
Python's MRO (method resolution order) can be very tricky for 
beginners.
In fact see how super init's parameter is being tossed around. 

The employee class is passing "name, age, gender, money, alive,
heartbeat" arguments through super. 

While Animal(which is next in the MRO) properly recieves 
all the arguments, it is passing only "name, age, gender, money"
to Super. 

Then,
(even though Person and Animal classes seem to be in the same 
hierarchy), the Person class recieves arguments passed from Animal.
(Try changing the arguments orders in Animal's super(), then you'll
see the Animal's attributes change by the order.)

This is actually due to how MRO's are architectured through Python, which follow
the C3 algorithm. 

# https://www.python.org/download/releases/2.3/mro/ <--- read here. 

Anyways my point is that, unless you are ready to track down the MRO
of python class inheritance, explicitly stating the arguments being
passed through __init__() might not be a good idea. 

We need a reliable and easy way to make this work. 
See next .py lecture! 
"""
