print("lesson 5 - 1")
# Напишите программу, которая принимает на вход список чисел и выводит на
# экран сумму всех элементов списка.
numbers = [1, 2, 5, 458, 15, -325, 0, 12.58, 6.568, -2.35, -152.]
i, summa = 0, 0
while i < len(numbers):
    summa += numbers[i]
    i += 1
print(f"Сумма чисел списка равна {summa}")
print()


print("lesson 5 - 2")
# Напишите программу, которая принимает на вход строку и выводит на экран
# количество гласных букв в ней.
# Гласными буквами считаются “а”, “е”, “и”, “о”, “у”, “ы”, “э”, “ю”, “я”.
text = input()
i, count = 0, 0
while i < len(text):
    if text[i].lower() in 'аеиоуыэюя':
        count += 1
    i += 1
print(f"Количество гласных в строке: {count}")
print()


print("lesson 5 - 3")
# Напишите программу, которая принимает на вход список слов и выводит на
# экран самое длинное слово из списка и его длину.
# Если таких слов несколько, выведите первое из них.
list_in = "Программа принимает на вход список слов и выводит самое длинное слово и его длину.".split()
print(list_in)
if len(list_in) == 0:
    print("Список пуст!")
else:
    i = 1
    word, len_word = list_in[0], len(list_in[0])
    while i < len(list_in):
        if len(list_in[i]) > len_word:
            word, len_word = list_in[i], len(list_in[i])
        i += 1
    print(f"Самое длинное слово в списке - '{word}', а его длина - {len_word}")
print()


print("lesson 5 - 4")
# Напишите программу, которая принимает на вход список чисел и выводит на экран новый список,
# в котором все четные числа умножены на 2, а все нечетные остались без изменений.
numbers = [1, 2, 5, 458, 15, -325, 0, 12, 58, 6, 568, -2, 35, -152]
# ------- вероятно имелось в виду - список целых чисел -------
print(numbers)
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        numbers[i] *= 2
    i += 1
print(numbers)
print()


print("lesson 5 - 5")
# Напишите программу, которая принимает на вход список чисел и выводит на
# экран индекс и значение минимального элемента в списке.
# Если таких элементов несколько, выведите первый индекс из них.
numbers = [1, 2, 5, 45.8, 15, -325, 0, 12, 5.8, 6, 56.8, -2, 35, -152., -325, 325, 45.6]
print(numbers)
if len(numbers) == 0:
    print("Список пуст!")
else:
    i = 1
    number, index = numbers[0], 0
    while i < len(list_in):
        if numbers[i] < number:
            number, index = numbers[i], i
        i += 1
    print(f"Индекс минимального элемента в списке - {index}, а его значение - {number}")
print()


print("lesson 5 - 6")
# Напишите программу, которая принимает на вход строку и выводит на экран новую строку,
# в которой все слова записаны в обратном порядке.
str_in = "Программа принимает на вход список слов и выводит самое длинное слово и его длину.".split()
# str_in = input().split()
print(str_in)

# срез
print(' '.join(str_in[::-1]))

# while
if len(str_in) == 0:
    print("Строка пуста!")
else:
    i = 0
    str_new = []
    while i < len(str_in):
        str_new.append(str_in[len(str_in) - 1 - i])
        i += 1
    print(' '.join(str_new))
print()
