"""
Python Classes. Basics
"""


class Car(object):

    def __init__(self, name, accelerator=False, brake=False,
                 steer=None, speed=0, direction=None):
        """
        The __init__ function of a class initializes the attritbutes
        of the class. Through the self argument, it sets the
        attributes indegenous to the class instance.

        What is an instance?
        Suppose we can come to an agreement on the common to a car.
        All cars behave in a similar fashion. You step on the accelerator
        it goes, step on the brake it stops.
        However all cars are distinct to each other. When I step
        on the accelerator of my car, my car will gain speed not other cars.
        It is because 'my car' and 'your car' are distinct beings even though
        they have common features. This existence of distinctivity is realized
        through the 'instance' in Python (or any object oriented programming).
        We create a 'class' which enables us to create multiple 'instances'
        which share common features. Just like a car!!!

        Coming back to the 'self' argument, the self explicitly states that
        a value of a attribute will only be applied to the distinct instance.
        Specifically the 'self.name' will allow the newly created instance
        to have its own name! Without the self, the name will not be indigenous
        to the instance.
        """
        self.name = name
        self.accelerator = accelerator
        self.brake = brake
        self.steer = steer
        self.speed = speed
        self.direction = direction

    def step_accel(self, step_on):
        """
        We can create functions which is only valid inside the class
        The step_accel function is only callable when the instance
        is a instance of the class 'Car'!
        Also by recieving the 'self' parameter to the function,
        we alter values of the instance by explicitly stating
        self.some_attribute = some_value"""
        self.accelerator = step_on
        print(f'current accelerator status is {self.accelerator}')
        if self.accelerator:
            self.speed += 1

    def step_brake(self, step_on):
        self.brake = step_on
        print(f'current brake status is {self.brake}')
        if self.brake:
            self.speed -= 1

    def steer_wheel(self, direction):
        self.steer = direction
        print(f'current steer status is {self.steer}')
        if self.steer:
            self.direction = self.steer

    def car_status(self):
        print(f"{self.name}'s speed is {self.speed} and direction is",
              f"{self.direction}")


if __name__ == '__main__':
    # remember name == main?
    # this prevents the code below from running when called by a
    # different module!
    # We want to use the Car class in ch3_1_2_classbasics.py
    # but we don't want the code below to be running!

    my_car = Car('Vroom Broom')
    """
    We create a car instance which which the variable name is 'my_car'
    It's variable name may be my_car but its name is 'Vroom Broom'
    """
    my_car.car_status()
    my_car.step_accel(True)
    my_car.car_status()
    my_car.steer_wheel('left')
    my_car.car_status()

    """
    See how we can change the values of the car instance easily by
    calling the class function"""

    your_car = Car('Babby')
    your_car.car_status()
    your_car.step_accel(True)
    your_car.car_status()
    your_car.steer_wheel('right')
    your_car.car_status()

    my_car.car_status()
    """
    There can be multiple instances of Car classes. We can confirm that
    applying a certain change to an instance does not affect the state of
    other instances. This can be extremely Convenient"""
