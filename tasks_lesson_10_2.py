# Своеобразное задание - что есть вычитание окружностей?
import math


class Circle:

    def __init__(self, radius: int | float):
        self.radius = radius

    def area(self) -> int | float:
        return math.pi * self.radius**2

    def __sub__(self, second):
        radius = abs(self.radius - second.radius)
        return Circle(radius) if radius else 'point'

    def __str__(self):
        return f'radius of circle {self.radius}'


c1 = Circle(25)
c2 = Circle(15)
c3 = Circle(25)

c4 = c1 - c2
c5 = c1 - c3

print(c3)
print(c4)
print(c5)
