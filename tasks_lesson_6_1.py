def root(x):
    # Напишите функцию root(x), которая возвращает квадрат своего аргумента.
    return x ** 2


def is_even(n):
    # Напишите функцию is_even(n), которая проверяет, является ли число четным или нечетным.
    # Функция должна возвращать True, если число четное, и False, если число нечетное.
    return n % 2 == 0


def factorial(n):
    # Напишите функцию factorial(n), которая вычисляет факториал своего аргумента.
    # Факториал числа n — это произведение всех натуральных чисел от 1 до n.
    # Например, factorial(4) = 4×3×2×1 = 24.
    # Функция должна возвращать факториал числа или -1, если число отрицательное.
    if n < 0:
        f = -1
    else:
        f = 1
        for i in range(1, n + 1):  # если мы проходили range()
            f *= i
    return f


def factorial_w(n):
    # Напишите функцию factorial(n), которая вычисляет факториал своего аргумента.
    # Факториал числа n — это произведение всех натуральных чисел от 1 до n.
    # Например, factorial(4) = 4×3×2×1 = 24.
    # Функция должна возвращать факториал числа или -1, если число отрицательное.
    if n < 0:
        f = -1
    else:
        f, i = 1, 1
        while i <= n:
            f *= i
            i += 1
    return f


def reverse(s):
    # Напишите функцию reverse(s), которая принимает строку s и возвращает ее в обратном порядке.
    # Например, reverse("hello") должна вернуть "olleh".
    return s[::-1]


def fibonacci(n):
    # Напишите функцию fibonacci(n), которая возвращает n-ый член
    # последовательности Фибоначчи. Первые два числа равны 1.
    f, f_next = 0, 1
    i = 1
    while i <= n:
        f += f_next
        f, f_next = f_next, f
        i += 1
    return f


def count_vowels(s):
    # Напишите функцию count_vowels(s), которая подсчитывает количество
    # гласных букв в строке s. Гласные буквы — это а, е, ё, и, о, у, ы, э, ю, я.
    # Например, count_vowels("привет") должна вернуть 2.
    count = 0
    for i in s:
        if i in 'аеёиоуыэюя':
            count += 1
    return count


def is_palindrome(s):
    # Напишите функцию is_palindrome(s), которая проверяет, является ли строка s палиндромом.
    # Палиндром — это слово или фраза, которая читается одинаково слева направо и справа налево.
    # Функция должна возвращать True, если строка палиндром, и False, если нет.
    return s.lower().replace(' ', '') == s[::-1].lower().replace(' ', '')


def power(x, n):
    # Напишите функцию power(x, n), которая возводит число x в степень n.
    return x ** n


def is_anagram(s1, s2):
    # Напишите функцию is_anagram(s1, s2), которая проверяет, являются ли две строки s1 и s2 анаграммами.
    # Анаграмма — это слово, составленное из перестановки букв другого слова.
    # Функция должна возвращать True, если строки анаграммы, и False, если нет.
    # Например, is_anagram("кот", "ток") должна вернуть True,
    # а is_anagram("кот", "собака") должна вернуть False.
    #
    #    if (len(s1.replace(',', '').replace('-', '').replace(':', '').replace(';', '')) !=
    #            len(s2.replace(',', '').replace('-', '').replace(':', '').replace(';', ''))):
    #
    # Вероятно множества не всегда будут работать - но попробую
    if len(s1) != len(s2):  # требует доработки по обработке Анаграмм, имеющих различную длину!!
        answer = False
    else:
        answer = True
        for letter in s1:
            if letter.lower() not in s2.lower():
                answer = False
                break
    return answer


def is_pangram(s):
    # Напишите функцию is_pangram(s), которая проверяет, является ли строка s панграммой или нет.
    # Панграмма — это строка, которая содержит все буквы алфавита хотя бы один раз.
    # Функция должна возвращать True, если строка панграмма, и False, если нет.
    # Например, "Аэрофотосъёмка ландшафта уже выявила земли богачей и процветающих крестьян." - True,
    # "Привет, мир!" - False.
    alfovit = 'абвгдеёжзийклмнопрстуфхцчшщьъыэюя'
    answer = True
    # text = list(set(s.lower()))
    # text.sort()
    for letter in alfovit:
        if letter not in s.lower():
            answer = False
            break
    return answer


print("lesson 6 - 1")
print(root(25))
print()

print("lesson 6 - 2")
print(is_even(666))
print(is_even(33))
print()

print("lesson 6 - 3")
print(factorial(4))
print(factorial(-4))
print()
print(factorial_w(4))
print(factorial_w(-4))
print()

print("lesson 6 - 4")
print(reverse('0123456789'))
print(reverse("hello"))
print(reverse("?nohtyP меачузи оншепсу ым"))
print()

print("lesson 6 - 5")
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(20))
print()

print("lesson 6 - 6")
print(count_vowels("привет"))
print(count_vowels("5"))
print(count_vowels("Напишите функцию, которая подсчитывает количество гласных букв в строке"))
print()

print("lesson 6 - 7")
print(is_palindrome("топот"))
print(is_palindrome("привет"))
print(is_palindrome("шабаш шабаш шабаш"))
print(is_palindrome("Лёша на полке клопа нашёл"))
print()

print("lesson 6 - 8")
print(power(5, 3))
print(power(2, 10))
print(power(3, 3))
print()

print("lesson 6 - 9")
# print(is_anagram("Аз есмь строка, живу я, мерой остр.", "За семь морей ростка я вижу рост."))
print(is_anagram("Я в мире — сирота.", "Я в Риме — Ариост."))
print(is_anagram("кот", "ток"))
print(is_anagram("кот", "напряжение"))
print()

print("lesson 6 - 10")
print(is_pangram("Аэрофотосъёмка ландшафта уже выявила земли богачей и процветающих крестьян"))
print(is_pangram("Привет, мир!"))
print()
