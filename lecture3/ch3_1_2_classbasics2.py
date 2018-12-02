"""
Saving Class instances and calling Class instances
"""

from ch3_1_1_classbasics import Car
# Note we can bring in Components from other modules if we
# have __init__.py initialized in the folder


class CarDatabase(object):

    def __init__(self):
        self.database = dict()

    def save(self, name, instance):
        self.database[name] = instance

    def delete(self, name):
        name = self.database.pop(name)
        print(f'instance {name} has been deleted')

    def retrieve(self, name):
        name = self.database[name]
        return name

    def retrieve_by_val(self, value):
        instance = None
        for name, instance in self.database.items():
            if value in instance.__dict__.values():
                instance = instance
        return instance

# Let's create a somewhat counter-intuitive case for classes

"""
We created a car database which saves car instances in a dictionary.
The key is the name of the instance, and the value is the instance
itself. 
The fun thing with classes is that you can create your own methods
then utilize them to your needs.  
Our CarDatabase() class also has methods already set to save, 
retrieve and search by values.
We just need to call the methods without the need to explicitly
writing down the method everytime
"""
car_tracker = CarDatabase()
# initialize our car database and anme it car_tracker

keon_car = Car('Broom Vroom')
you_car = Car('hello')
poo_car = Car('poop')
# create our car instance 'keon_car' and name it 'Broom Vroom'
car_tracker.save('keon_car', keon_car)
car_tracker.save('poo_car', poo_car)
car_tracker.save('you_car', you_car)

print(car_tracker.__dict__)

# save our car instance into the car_tracker database

some_car = car_tracker.retrieve('keon_car')
print(f'class instance itself: {some_car},',
      f' values stored: {some_car.__dict__}')
"""
See how we can retrieve 'keon_car' and see the values inside
by callind the .__dict__ method of the class.
In fact, all class instances can be converted into a 'dict'
because the class object has a built in__dict__ method
"""

some_car.car_status()
some_car.step_accel(True)
some_car.car_status()
some_car.steer_wheel('left')
some_car.car_status()
# We can perform class functions already from the retrieved instances

car_tracker.save('keon_car', some_car)
# we override the already existing instance with key 'keon_car'
# then save it into the database again

some_car = car_tracker.retrieve('keon_car')
print(f'class instance itself: {some_car},',
      f' values stored: {some_car.__dict__}')
# when we retrieve our overidden instance again we see that the change has
# been applied

keons_car = car_tracker.retrieve_by_val('Broom Vroom')
# we have also created a method to retrieve the instance by a given value
# See how we retrieve the instance by the attribute of the instance
print(keons_car.__dict__)
