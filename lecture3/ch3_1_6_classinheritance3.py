"""
Python Basic Multiple Inheritance and Use case of
*args and **kwargs
"""


class Person(object):

    def __init__(self, *args, **kwargs):
        super(Person, self).__init__()
        self.name = kwargs.get('name', None)
        self.age = kwargs.get('age', None)
        self.gender = kwargs.get('gender', None)

    def tell_person_attribute(self):
        print(f'{self.name}, is a {self.gender}, and is {self.age} years old')


class EmploymentMIXIN(object):

    def __init__(self, *args, **kwargs):
        super(EmploymentMIXIN, self).__init__()
        self.position = kwargs.get('position', None)
        self.salary = kwargs.get('salary', 0)
        self.company = kwargs.get('company', None)

    def empolyment_status(self):
        print(f'{self.name} works for {self.company} as {self.position}.')


class SocialPerson(Person, EmploymentMIXIN):

    def __init__(self, *args, **kwargs):
        super(SocialPerson, self).__init__(*args, **kwargs)

    def social_person_status(self):
        print(f'{self.name}, is a {self.gender}, and is {self.age} years old')
        print(f'{self.name} works for {self.company} as {self.position}.')


keon = SocialPerson(name='keon', age='24', gender='Male',
                    position='graduateschoolslave')

keon.social_person_status()
keon.empolyment_status()

"""
See how everything is being passed around with only *args and **kwargs.
Without the need to track the order of MRO, the inheritance to works by
all classes receiving all the parameters passed on by the top level
class. All classes just cherry pick what they need! 

In fact, this can be a very effective way to implement Multiple
inheritance. 

"""
