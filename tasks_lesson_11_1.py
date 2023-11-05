# Класс Soda (для определения типа газированной воды)
class Soda:
    def __init__(
            self,
            additive=None
    ):

        self.additive = additive

    def show_my_drink(self) -> None:
        if self.additive is None:
            print("Обычная газировка")
        else:
            print(f"Газировка и {self.additive}")


drink_1 = Soda('сироп')
drink_1.show_my_drink()
drink_2 = Soda()
drink_2.show_my_drink()
print('----------------')
print()


# Класс TriangleChecker (возможность построения треугольника из отрезков представленной длины)
class TriangleChecker:
    def __init__(
            self,
            a: int | float,
            b: int | float,
            c: int | float
    ):

        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float)):
            if self.a > 0 and self.b > 0 and self.c > 0:
                if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                    return "Ура, можно построить треугольник!"
                else:
                    return "Жаль, но из этого треугольник не сделать."
            else:
                return "С отрицательными числами ничего не выйдет!"
        else:
            return "Нужно вводить только числа!"


triangle_1 = TriangleChecker(2, 5, 9)
triangle_2 = TriangleChecker(2, 2, 3)
triangle_3 = TriangleChecker('a', 5, 9)
triangle_4 = TriangleChecker(2, '5', 9)
triangle_5 = TriangleChecker(2, 5, '9')
triangle_6 = TriangleChecker(-2, 5, 9)
triangle_7 = TriangleChecker(2, -5, 9)
triangle_8 = TriangleChecker(2, 5, -9)
triangle_9 = TriangleChecker('2', 5, -9)
triangle_10 = TriangleChecker(4, 2, 3)

print(triangle_1.is_triangle())
print(triangle_2.is_triangle())
print(triangle_3.is_triangle())
print(triangle_4.is_triangle())
print(triangle_5.is_triangle())
print(triangle_6.is_triangle())
print(triangle_7.is_triangle())
print(triangle_8.is_triangle())
print(triangle_9.is_triangle())
print(triangle_10.is_triangle())
print('----------------')
print()


# Класс KgToPounds (перевод килограмм -> фунт)
class KgToPounds:
    def __init__(self, kg: int | float):
        self.__kg = kg

    def to_pounds(self):
        # 1 kg = 2.2046226 фунта lb
        return self.__kg * 2.2046226

    def set_kg(self, kg: int | float):
        self.__kg = kg

    def get_kg(self):
        return self.__kg


weight_1 = KgToPounds(1)
weight_2 = KgToPounds(5)
weight_3 = KgToPounds(2.2679618724765)

print(weight_1.to_pounds())
print(weight_2.to_pounds())
print(weight_3.to_pounds())

weight_new = KgToPounds(20)
print(weight_new.get_kg())
print(weight_new.to_pounds())
weight_new.set_kg(25)
print(weight_new.get_kg())
print(weight_new.to_pounds())
# print(dir(weight_new))
print(weight_new._KgToPounds__kg)
print('----------------')
print()


# !! Класс KgToPoundsNew (перевод килограмм -> фунт) с проверкой ИД
class KgToPoundsNew:
    def __init__(self, kg: int | float):
        if type(kg) in (int, float):
            self.__kg = kg
        else:
            print("Вес должен быть числом! Введена -", type(kg))
            self.__kg = 'error'

    def to_pounds(self):
        # 1 kg = 2.2046226 фунта lb
        if type(self.__kg) in (int, float):
            return self.__kg * 2.2046226
        else:
            return "Вес должен быть числом!"

    def get_kg(self):
        return self.__kg

    def set_kg(self, kg: int | float):
        if type(kg) in (int, float):
            self.__kg = kg
        else:
            print("Вес должен быть числом! Введена -", type(kg))
            self.__kg = 'error'


weight_1 = KgToPoundsNew(-1)
weight_2 = KgToPoundsNew(5)
weight_3 = KgToPoundsNew(2.2679618724765)
weight_4 = KgToPoundsNew('5')

print('1', weight_1.to_pounds())
print('2', weight_2.to_pounds())
print('3', weight_3.to_pounds())
print('4', weight_4.to_pounds())

weight_new = KgToPoundsNew(20)
print('6', weight_new.get_kg())
print('7', weight_new.to_pounds())
weight_new.set_kg('25')
print('8', weight_new.get_kg())
print('9', weight_new.to_pounds())
print('----------------')
print()


# !!! Класс KgToPoundsNewDec (перевод килограмм -> фунт) с проверкой ИД и декораторами
class KgToPoundsNewDec:
    def __init__(self, kg: int | float):
        if type(kg) in (int, float):
            self.__kg = kg
        else:
            print("Вес должен быть числом! Введена -", type(kg))
            self.__kg = 'error'

    def to_pounds(self):
        # 1 kg = 2.2046226 фунта lb
        if type(self.__kg) in (int, float):
            return self.__kg * 2.2046226
        else:
            return "Вес должен быть числом!"

    @property
    # ----- Геттер -----
    def kg(self):
        return self.__kg

    @kg.setter
    # ----- Сеттер -----
    def kg(self, kg: int | float):
        if type(kg) in (int, float):
            self.__kg = kg
        else:
            print("Вес должен быть числом! Введена -", type(kg))
            self.__kg = 'error'


weight_1 = KgToPoundsNewDec(-1)
weight_2 = KgToPoundsNewDec(5)
weight_3 = KgToPoundsNewDec(2.2679618724765)
weight_4 = KgToPoundsNewDec('5')

print('1', weight_1.to_pounds())
print('2', weight_2.to_pounds())
print('3', weight_3.to_pounds())
print('4', weight_4.to_pounds())

weight_new = KgToPoundsNewDec(20)
print('6', weight_new.kg)
print('7', weight_new.to_pounds())
weight_new.kg = '25'
print('8', weight_new.kg)
print('9', weight_new.to_pounds())
weight_new.kg = 25
print('10', weight_new.kg)
print('11', weight_new.to_pounds())
print('----------------')
print()
