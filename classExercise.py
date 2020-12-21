
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

# *****************************
# *****************************
# * Some Practices

# *  Text formmating using %
myName = 'Mehrnoush'
myAge = 38
someText = 'My name is %s and I am %s' % (myName, myAge)
print(someText)

# * Multi-Line Text
myString = '''This is 
Multi line '''
print(myString)

# * Python Ternary
print('Hello') if myAge < 38 else print('Goodby')

# * Using Trye    Except    Finally    in For Loops
i = 0
for i in range(5):
    print('----------------')
    try:
        print(10 / (i - 3))
    except ZeroDivisionError:
        print('Division by zero')
    finally:
        print('I am awsome')
    print(i)

# * Enumerate function in For Loops
my_name = 'Mehrnoush'
for i, c in enumerate(my_name):
    print(i, c)

# * Create a rectangle class
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
    def peremiter(self):
        return 2 * (self.height + self.width)

my_rectangle = Rectangle(30, 50)
print(my_rectangle.area())
print(my_rectangle.peremiter())