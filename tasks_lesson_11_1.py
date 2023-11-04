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

print()


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
