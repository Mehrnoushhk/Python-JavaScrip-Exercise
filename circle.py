import math

class Circle:
    def __init__(self, radius: float = 1):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.radius = radius
        self.diameter = 2 * self.radius

    def __setattr__(self, key, value):
        if key == 'radius':
            if value < 0:
                raise ValueError('Radius cannot be negative')
            self.__dict__[key] = value
            self.__dict__['diameter'] = 2 * self.radius

        elif key == 'diameter':
            if value < 0:
                raise ValueError('Diameter cannot be negative')
            self.__dict__[key] = value
            self.__dict__['radius'] = self.diameter / 2
        else:
            raise AttributeError
    @property
    def area(self):
        return math.pi * (self.radius ** 2)


    def __str__(self):
        return f'Circle({int(self.radius)})'

    def __repr__(self):
        return f'Circle({int(self.radius)})'


# c = Circle(2)
# print(c.diameter)
# print(c.area)