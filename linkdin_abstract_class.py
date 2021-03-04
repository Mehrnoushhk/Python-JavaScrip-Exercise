from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Graphicshape(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calc_area(self):
        pass

class Circle(Graphicshape, JSONify):
    def __init__(self, radious):
        self.radious = radious
    def calc_area(self):
        return (self.radious ** 2) * 3.14
    def toJSON(self):
        pass

circle_1 = Circle(10)
print(circle_1.calc_area())