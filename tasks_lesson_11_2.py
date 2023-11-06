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


# Класс Person (для обработки персоналии)
class Person:
    def __init__(self, name: str, age: int | float, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}'

    def get_name(self):
        return self.name

    @property
    def set_name(self, new_name: str):
        self.name = new_name

    @staticmethod
    def is_adult(self):
        return self.age >= 18

    @classmethod
    def create_from_string(cls, s: str):
        name, age, gender = s.split('-')
        return cls(name, age, gender)


person_1 = Person("Bob", 8, 'm')
person_2 = Person('Alina', 16, 'f')
person_3 = Person('Pol', 34, 'm')
person_4 = Person('Nadin', 42, 'f')
person_cls_1 = "Oleg-29-m"
person_cls_2 = "Olga-22-f"

print(person_4)
print(person_3.get_name())
person_4.name = 'Elis'
print(person_4)
print(Person.is_adult(person_2))
print(Person.is_adult(person_4))
print(Person.is_adult(person_1))
print(person_1)
print(person_4)
print(person_1.get_name())
person_1.name = 'Serge'
print(person_1)
person_1.name = 'Serёga'
print(person_1)
print(person_1.get_name())
print(Person.create_from_string(person_cls_1))
print(Person.create_from_string(person_cls_2))
print('----------------')
print()
