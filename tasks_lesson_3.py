print("lesson 3 - task 01")
# Создайте список с именами трех цветов и выведите его на экран.
color = ['red', 'grin', 'blue']
print(color)
print(*color)
print()


print("lesson 3 - task 02")
# Создайте словарь с ключами “name”, “age” и “city” и присвойте им
# произвольные значения. Выведите на экран значение ключа “city”.
person = {'name': 'Pol', 'age': 33, 'city': 'Brest'}
print(person['city'])
print()


print("lesson 3 - task 03")
# Создайте строку с текстом “Привет, мир!” и выведите на экран ее длину.
message = 'Привет, мир!'
print(len(message))
print()


print("lesson 3 - task 04")
# Создайте переменную с числом 42 и выведите на экран его квадратный корень.
number = 42
print(number ** (1/2))
print()


print("lesson 3 - task 05")
# Создайте список с числами от 1 до 10 и выведите на экран сумму всех элементов списка.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
suma = (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6] + numbers[7]
        + numbers[8] + numbers[9])
print(suma)

numbers_ = [i for i in range(1, 11)]
print(numbers_)
suma_ = sum(numbers_)
print(suma_)
print()


print("lesson 3 - task 06")
# Создайте словарь с ключами “a”, “b” и “c” и присвойте им значения 1, 2 и 3
# соответственно. Выведите на экран произведение значений ключей “a” и “c”.
literals = {"a": 1, "b": 2, "c": 3}
print(literals["a"] * literals["c"])
print()


print("lesson 3 - task 07")
# Создайте строку с текстом “Python это интересный язык программирования”
# и выведите на экран ее первые пять символов.
message_ = "Python это интересный язык программирования"
print(message_[:5])
print()


print("lesson 3 - task 08")
# Создайте список с числами 12, 15, 18, 21 и 24 и выведите на экран
# остаток от деления каждого элемента списка на 5.
numbers__ = [12, 15, 18, 21, 24]
print(numbers__[0] % 5)
print(numbers__[1] % 5)
print(numbers__[2] % 5)
print(numbers__[3] % 5)
print(numbers__[4] % 5)
print()

for i in range(len(numbers__)):
    print("остаток от деления ", i+1, "-го числа на 5 равен ",
          numbers__[i] % 5, sep='')
print()

for i in range(len(numbers__)):
    print("остаток от деления {0}-го числа на 5 равен {1}".format(i+1, numbers__[i] % 5))
print()

for i in range(len(numbers__)):
    print(f"остаток от деления {i+1}-го числа на 5 равен {numbers__[i] % 5}")
print()


print("lesson 3 - task 09")
# Создайте словарь с ключами “x”, “y” и “z” и присвойте им значения 10, 20 и 30 соответственно.
axes = {}
axes['x'] = 10
axes['y'] = 20
axes['z'] = 30
print(axes)
print()


print("lesson 3 - task 10")
# Выведите на экран целочисленное деление значения ключа “z” на значение ключа “x”.
print(axes['z'] // axes['x'])
print()


print("lesson 3 - task 11")
# Создайте список с именами трех фруктов и вложите его в словарь с ключом “fruits”.
# Выведите на экран значение ключа “fruits”.
fruits = ['banana', 'orange', 'apple']
new_dic = {'fruits': fruits}
print(new_dic)

axes['fruits'] = fruits
print(axes)
print()


print("lesson 3 - task 12")
# Создайте словарь с ключами “name” и “age” и присвойте им произвольные значения.
# Вложите этот словарь в другой словарь с ключом “person”.
# Выведите на экран значение ключа “age” из вложенного словаря.
person_ = {'name': 'Ali', 'age': 22}
new_dic['person'] = person_
# print(new_dic)
print(new_dic['person']['age'])
print()


print("lesson 3 - task 13")
# Создайте словарь с ключами “name” и “hobby” и присвойте им произвольные значения.
# Вложите этот словарь в другой словарь с ключом “person”.
# Выведите на экран значение ключа “hobby” из вложенного словаря.
person__ = {'name': 'Ale', 'hobby': 'read'}
new_dic['person'] = person__
# print(new_dic)
print(new_dic['person']['hobby'])
print()


print("lesson 3 - task 14")
# Создайте словарь с ключами “name” и “scores” и присвойте им произвольные значения.
# Значение ключа “scores” должно быть списком с тремя числами.
# Выведите на экран среднее арифметическое этих чисел.
person___ = {'name': 'Bob', 'scores': [24, 66, 99]}
print(sum(person___['scores']) / len(person___['scores']))
print()


print("lesson 3 - task 15")
# Создайте список с двумя элементами.
# - первый элемент должен быть строкой с текстом “Hello”;
# - второй элемент должен быть словарем с ключами “world” и “!” и значениями 1 и 2 соответственно.
# Выведите на экран значение ключа “!” из словаря, который является вторым элементом списка.
new_list = ['Hello', {'world': 1, '!': 2}]
print(new_list[1]['!'])
print()


print("lesson 3 - task 16")
# Создайте список с тремя элементами.
# - первый элемент должен быть числом 10;
# - второй элемент должен быть строкой с текстом “Hello”;
# - третий элемент должен быть словарем с ключами “a” и “b” и значениями 3 и 4 соответственно.
# Выведите на экран сумму первого элемента списка и значения вложенного словаря по ключу “a”.
new_list_ = [10, 'Hello', {'a': 3, 'b': 4}]
print(new_list_[0] + new_list_[2]['a'])
print()


print("lesson 3 - task 17")
# Создайте список с четырьмя элементами.
# - первый элемент должен быть числом 5;
# - второй элемент должен быть строкой с текстом “World”;
# - третий элемент должен быть словарем с ключами “a” и “b” и значениями 6 и 7 соответственно;
# - четвертый элемент должен быть вложенным списком с двумя числами 8 и 9.
# Добавьте во вложенный словарь новый ключ “new” со значением 223.
# Добавьте число 10 во вложенный список.
list_17 = [5, 'World', {'a': 6, 'b': 7}, [8, 9]]
# print(list_17)
list_17[2]['new'] = 223
list_17[3].append(10)
print(list_17)
print()


print("lesson 3 - task 18")
# Создайте словарь с ключами “name” и “info” и присвойте им произвольные значения.
# Значение ключа “info” должно быть словарем с ключами “age”, “city” и “hobbies”.
# Значение ключа “hobbies” должно быть списком с тремя строками.
# Выведите на экран вторую строку из списка, который является значением ключа “hobbies” из словаря,
# который является значением ключа “info” из первого словаря.
dict_18 = {'name': 'Pol',
           'info': {"age": 22, 'city': 'Minsk', 'hobbies': ['read', 'write', 'coding']}
           }
print(dict_18['info']['hobbies'][1])
print()


print("lesson 3 - task 19")
# Создайте словарь с ключами “name” и “friends” и присвойте им произвольные значения.
# Значение ключа “friends” должно быть списком с тремя словарями.
# Каждый словарь должен иметь ключи “name” и “age” и произвольные значения.
# Выведите на экран имя и возраст первого друга из списка,
# который является значением ключа “friends” из первого словаря.
dict_19 = {'name': 'Ali',
           'friends': [
               {"name": 'Ale', 'age': 22},
               {"name": 'Bob', 'age': 20},
               {"name": 'Pol', 'age': 30}]
           }
# print(dict_19)
print(dict_19['friends'][0]['name'], dict_19['friends'][0]['age'])
print()
