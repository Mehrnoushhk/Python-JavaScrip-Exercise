
# * Example 1
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " now is sitting")
    def rollOver(self, ntimes):
        print('{} is rolled over {} times'.format(self.name.title(), str(ntimes)))

# myDog = Dog('drago', 2)
# print('{} is {} years old'.format(myDog.name.title(), str(myDog.age)))
# myDog.sit()
# myDog.rollOver(5)

# * Example 2
# * Define car object with 2 properties (speed, brand, model) and 3 methods (breake, accelerate, describe, decelerate)

class Car():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.motion = 'The car is at rest'
    def motionCheck(self):
        if self.speed > 0:
            self.motion = 'The car is moving'
        else:
            self.motion = 'The car is at rest'
    def accelerate(self, amount):
        self.speed += amount
        self.motionCheck()
    def decelerate(self, amount):
        if amount <= self.speed:
            self.speed -= amount
        else:
            self.speed = 0
        self.motionCheck()
    def breake(self):
        self.speed = 0
        self.motionCheck()
    def describe(self):
        print('My car brand is {} and its model is {} and {}'.format(self.brand, self.model, self.motion))


myCar = Car('BMW', 'X6')
print(myCar.describe())
myCar.accelerate(100)
print('Speed is {}'.format(str(myCar.speed)))
print(myCar.describe())
myCar.decelerate(60)
print('Speed is {}'.format(str(myCar.speed)))
print(myCar.describe())
myCar.breake()
print('Speed is {}'.format(str(myCar.speed)))
print(myCar.describe())

