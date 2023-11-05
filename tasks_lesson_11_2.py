# Класс RealString (для сравнения строк)
class RealString:
    def __init__(self, text: str):
        self.text = text

#    def __eq__(self, other: str):
#        if isinstance(other, RealString):
#            return len(self.text) == len(other.text)
#        else:
#            return len(self.text) == len(str(other))

    def __eq__(self, other: str):
        if isinstance(other, RealString):
            res = len(self.text) == len(other.text)
        else:
            res = len(self.text) == len(str(other))
        if res is True:
            return "Длинна строк одинакова"
        else:
            return "Длинна строк различна"


str_1 = RealString('fish')
str_2 = RealString('Fish')
str_3 = RealString('dog')
str_4 = RealString('Apple')

print(str_1 == str_2)
print(str_3 == str_2)
print(str_1 == str_3)
print(str_4 == str_3)
print(str_4 == '123')
print('Orange' == str_3)
print('Orange 123' == str_3)
print(str_3 == 123)
print('----------------')
print()


# Класс Rectangle (для обработки прямоугольников)
class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Прямоугольник с шириной {self.width} и высотой {self.height}'

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    @property
    def is_square(self):
        return self.height == self.width


figura_1 = Rectangle(2, 8)
figura_2 = Rectangle(12, 8)
figura_3 = Rectangle(2, 18)
figura_4 = Rectangle(2, 2)

print(figura_4)
print(figura_3.get_area())
print(figura_2.get_perimeter())
print(figura_1.is_square)
print(figura_4.is_square)
print('----------------')
print()
