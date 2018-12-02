"""
Saving class instances without saving the instance itself
"""
from random import randrange
# python built_in methods

from ch3_1_1_classbasics import Car
# import car


class CarDatabaseNoInstanceSave(object):

    def __init__(self):
        """
        We have a dict which holds the data of cars. 
        In this case, we work on the premise that the keys can
        only be a certain number.
        Then we need to keep a list of numbers that are already taken
        to make our data adding process more efficient. 
        Imagine we already have 1 to 1000 numbers taken, if we don't have
        a list, then we will have run a for_loop which repeats until it finds
        a number which is not taken. 
        Having a used_primary_key list saves us from the hassle 
        """
        self.database = dict()
        self.used_primary_key = list()

    def save(self, instance, update=False, primary_key=False):
        """
        To save the instance and give it a number, we find that last 
        number number of the primary key list 
        (which we assume that the list will increment by 1 everytime
        we add a number. And that is exactly how we made it)
        After that we open up the class instance and save them in list form.
        """
        if not update:
            try:
                num_to_add = int(self.used_primary_key[-1]) + 1
            except IndexError:
                num_to_add = 0
            # In fact this is how we handle errors which we know will happen
            # We know that if there is no value yet in the primary_key list
            # then there will be no index matching -1.
            # This is a known problem which we can let it pass!
        else:
            num_to_add = primary_key
            # If we are updating the instance then we just override it by the
            # key!

        index_dict = {'name': 0, 'accelerator': 1, 'brake': 2,
                      'steer': 3, 'speed': 4, 'direction': 5}

        list_to_add_data = [None, None, None, None, None, None]
        for key, value in instance.__dict__.items():
            list_to_add_data[index_dict[key]] = value

        self.database[num_to_add] = list_to_add_data

        self.used_primary_key.append(num_to_add)
        # We then append our number to the list!

    def delete(self, primary_key):
        del_instance = self.database.pop(primary_key)
        print(f'instance {del_instance.__dict__} has been deleted')

    def retrieve(self, primary_key):
        try:
            data_by_list = self.database[primary_key]
        except IndexError:
            print(f'the database does not have',
                  f' any data with primary_key : {primary_key}')
        # This also we know that we can have cases which the user
        # does not recall the index number properly! We just warn the user
        # That there is no matching value!

        instance = Car(data_by_list[0], data_by_list[1], data_by_list[2],
                       data_by_list[3], data_by_list[4], data_by_list[5])
        return instance

"""
What we did here is created a CarDatabase like the last module
But it does not store the class instance iteself. 
It only holds a dictionary which looks like the following
{number as key : list of values by order}
In fact, this is an extremely rudimentary way how an middleware would
operate. The database saves data differently than how python may
use them. Then we need a middleware to link the two different structures.
Read comments in the class to understand what is happening
"""

car_tracker = CarDatabaseNoInstanceSave()
# initialize our car database and anme it car_tracker

Broom_Vroom = Car('Broom Vroom')
# create our car instance 'keon_car' and name it 'Broom Vroom'

car_tracker.save(Broom_Vroom)
# save our car instance into the car_tracker database

some_car = car_tracker.retrieve(0)
print(f'class instance itself: {some_car},',
      f' values stored: {some_car.__dict__}')

some_car.car_status()
some_car.step_accel(True)
some_car.car_status()
some_car.steer_wheel('left')
some_car.car_status()
# We can perform class functions already from the retrieved instances


car_tracker.save(some_car, update=True, primary_key=0)
# We are updating the already existing car Broom_Vroom!


car_tracker.save(Car('Hey Car'))
# We can even save the car instance by just initializing it in the
# save function!

hey_car = car_tracker.retrieve(1)
print(f'class instance itself: {hey_car},',
      f' values stored: {hey_car.__dict__}')
