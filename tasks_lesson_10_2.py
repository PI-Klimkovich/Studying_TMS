# Своеобразное задание - что есть вычитание окружностей?
import math


class Point:

    def __init__(self, x: int | float, y: int | float):
        self.x = x
        self.y = y

    def __str__(self):
        return f'point coordinates ({self.x}, {self.y})'


class Circle:

    def __init__(self, radius: int | float):
        self.radius = radius

    def area(self) -> int | float:
        return math.pi * self.radius**2

    def __sub__(self, other):
        radius = abs(self.radius - other.radius)
        return Circle(radius) if radius else Point(0, 0)

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
