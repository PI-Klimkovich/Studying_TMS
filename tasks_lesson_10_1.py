from time import sleep


class Auto:
    def __init__(
            self,
            brand,
            age,
            mark,
            color=None,
            weight=None
    ):

        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self) -> None:
        print('move')

    def birthday(self) -> int:
        return self.age + 1

    def stop(self) -> None:
        print('stop')


# bus1 = Auto("MAZ", 5, '231')
# bus2 = Auto("MAZ", 8, '232', color='red')
# bus3 = Auto("ПAZ", 11, '32053-70 ШКОЛЬНЫЙ', color='yellow')
# bus4 = Auto("ПAZ", 11, 'CITYMAX 9', color='white', weight=2650)

# print(bus1.mark)
# print(bus2.color)
# bus1.move()
# print(bus2.age)
# print(bus2.birthday())
# bus3.stop()
# print(bus4.brand)
# print(bus1.weight)
# bus4.move()
# print(bus4.birthday())

class Truck(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_load: int, *args, **kwargs):
        super().__init__(brand, age, mark, *args, **kwargs)
        self.max_load = max_load

    def move(self) -> None:
        print("attention move")

    def load(self) -> None:
        sleep(1)
        print('load')
        sleep(1)


truck1 = Truck("MAZ", 5, '5440C5', 25000)
truck2 = Truck("MAZ", 8, '643028', 30000, color='red')
truck3 = Truck("KAMAZ", 12, '4308-81 (N5)', 40000, color='green', weight=5200)
truck4 = Truck("KAMAZ", 2, '43118-50', 50000, color='white', weight=6200)

print(truck1.brand)
print(truck2.birthday())
truck4.move()
truck3.load()
truck3.stop()
print(truck4.birthday())
