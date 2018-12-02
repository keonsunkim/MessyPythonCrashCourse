"""
Python Basic Class Inheritance Basics
"""


class Vehicle(object):
    """
    Suppose we want to classes: Car and a Motorcycle
    A car and a motorcycle has similar attributes while
    they also have conspicuous distinctions.

    Let's say that we have we can come to a conclusion
    on the Car and the Motorcycle's common ground.
    Then we can actually save ourselves from repeating
    ourselves if we can set that certain common ground first
    and let the Car and Motorcycle reference to it.

    Not to mention that fixing things will become much more easier.
    Change an attribute in the reference, the change will be
    applies to all types of vehicles.

    That is the exact reason why we use a class inheritance.
    This Vehicle class will be the base class to both
    Car and Motorcycle
    """

    def __init__(self, name, type_vehicle, speed=None, direction=None):
        self.type_vehicle = type_vehicle
        self.name = name
        self.speed = speed
        self.direction = direction

    def vehicle_speed(self):
        print(f"{self.name}'s speed is {self.speed}")

    def vehicle_direction(self):
        print(f"{self.name}'s direction is {self.direction}")

    def vehicle_status(self):
        print(f"{self.name}'s speed is {self.speed} and direction is",
              f"{self.direction}")


class Car(Vehicle):
    """
    See how we did not set object as the Car class's argument.
    We explictly stated that the Vehicle class as the class's
    argument.

    This is telling python that we will be building on top of the
    Vehicle class. We will have the Vehicle class's methods and
    attributes all availible to us.
    """

    def __init__(self, name, speed=0, direction=None,
                 accelerator=None, steer_wheel=None, brake=None):
        """
        Extending the base class is the quintessential element
        of class inheritance.

        This means that we will need to allow our parent class
        know about the attributes we are receiving.

        The super() method calls the parent class directly
        above this class to be initialized.
        """
        super(Car, self).__init__(name, 'car', speed, direction)

        self.accelerator = accelerator
        self.steer_wheel = steer_wheel
        self.brake = brake

    def __str__(self):
        """
        Here I introduce another built in class method.
        The __str__ method allows the class instance to 
        have a certain name (human readable) 
        instead of some <model instance... > form
        """
        return(f'this car is {self.name}')

    def control_speed(self, accelerator=False, brake=False):
        if accelerator:
            self.accelerator = accelerator
            self.brake = False
            self.speed += 1
        elif brake:
            self.brake = brake
            self.accelerator = False
            self.speed = 0
        else:
            print('use a accelerator or a brake!')

    def steer_car_wheel(self, steer_wheel=None):
        """
        By declaring a method in the child class
        we can create a method only availible to the
        child class.
        """
        self.steer_wheel = steer_wheel
        if self.steer_wheel:
            self.direction = self.steer_wheel

    def vehicle_status(self):
        """
        When we define the method already given in the 
        parent class in the child class, we call this 
        overriding the class method.
        We change the behaviour of the parent class's 
        method. 

        We can also override the parent class's method while
        keeping the functionalities of the parent class's method.
        Simply call with super.
        super().__method_name__() will allow the parent class's 
        method to run first then have the changed behavior run.
        """
        super(Car, self).vehicle_status()
        print(f"{self.name}'s steering wheel is set on {self.steer_wheel} "
              f"currently the {'accelerator' if self.accelerator else 'brake'} is activated")


my_car = Car('broom_vroom')
# We initiate a Car class instance!

my_car.vehicle_status()
my_car.control_speed(accelerator=True, brake=False)
my_car.vehicle_status()
my_car.steer_car_wheel('left')
my_car.control_speed(accelerator=False, brake=True)
# my_car.steer_wheel(steer_wheel='left')

my_car.vehicle_status()
# We can perform class methods just like when we created a class
# without any class inheritance!

print(my_car)
# see how now the representation of the model is not something like
# <model at ~~ 000x16D>. This is due to the changes done by the
# __str__ method!
