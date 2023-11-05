# Класс RealString (для сравнения строк)
class RealString:
    def __init__(self, text: str):
        self.text = text

    def __eq__(self, other: str):
        if isinstance(other, RealString):
            return len(self.text) == len(other.text)
        else:
            return len(self.text) == len(str(other))


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
