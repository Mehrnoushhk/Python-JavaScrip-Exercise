class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " now is sitting")
    def rollOver(self, ntimes):
        print('{} is rolled over {} times'.format(self.name.title(), str(ntimes)))

myDog = Dog('drago', 2)
print('{} is {} years old'.format(myDog.name.title(), str(myDog.age)))
myDog.sit()
myDog.rollOver(5)
