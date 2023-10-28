print("lesson 8 - 1")
# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий только четные числа из исходного списка.
# Используйте функцию filter и лямбда-выражение.
numbers = [5, 0, 16, 99, -18, 5, -55, 15, -6, 0, 20, 10, -3]
print(numbers)
numbers_new = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers_new)
print()

print("lesson 8 - 2")
# Напишите код, который принимает список кортежей вида (имя, возраст)
# и возвращает новый список, отсортированный по возрастанию возраста.
# Используйте функцию sorted и ключ сортировки.
persons = [('Vano', 29), ('Vada', 19), ('Anna', 18), ('Pol', 49), ('Bob', 19), ('Serg', 25), ('Max', 2)]
print(persons)
persons_sort = sorted(persons, key=lambda x: x[1])
print(persons_sort)
print()

print("lesson 8 - 3")
# Напишите код, который принимает список строк и возвращает новый список,
# содержащий только те строки, которые начинаются с гласной буквы. (Да да, снова эти гласные)
# Используйте функцию filter и множество.
sentences = [
    "Напишите код, который принимает список строк и возвращает новый список.",
    "Да да, снова эти гласные.",
    "Используйте функцию filter и множество.",
    "Аэрофотосъёмка ландшафта уже выявила земли богачей и процветающих крестьян.",
    "Привет, мир!",
    "Я в Риме — Ариост."
]
for _ in sentences:
    print(_)
sentences_new = list(filter(lambda x: x[0].lower() in 'аеёиоуыэюя', sentences))
print(sentences_new)
print()

print("lesson 8 - 4")
# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий квадраты этих чисел. Используйте функцию map и lambda.
print(numbers)
numbers_new = list(map(lambda x: x ** 2, numbers))
print(numbers_new)
print()

print("lesson 8 - 5")
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по убыванию длины слов.
# Используйте функцию sorted и обратный порядок сортировки.
words = ['Аэрофотосъёмка', 'ландшафта', 'уже', 'выявила', 'земли', 'богачей', 'и', 'процветающих', 'крестьян']
print(words)
words_new = sorted(words, key=lambda x: len(x), reverse=True)
print(words_new)
print()

print("lesson 8 - 6")
# Напишите код, который принимает строку и возвращает список,
# содержащий только те буквы, которые встречаются в слове “python”.
# Используйте функцию filter и оператор in.
text = 'Python lists have a built-in list.sort() method that modifies the list in-place.'
print(text)
text_new = list(filter(lambda x: x.lower() in 'python', text))
print(text_new)
print()

print("lesson 8 - 7")
# Напишите код, который принимает список чисел и возвращает новый список,
# содержащий эти же числа, умноженные на 10. Используйте функцию map.
print(numbers)
numbers_new = list(map(lambda x: x * 10, numbers))
print(numbers_new)
print()

print("lesson 8 - 8")
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по алфавиту. Используйте функцию sorted.
print(words)
words_new = sorted(words)
print(words_new)
print()

print("lesson 8 - 9")
# Напишите функцию, которая принимает список строк и возвращает новый
# список, содержащий только те строки, которые являются палиндромами.
# Палиндром — это слово, которое читается одинаково слева направо и справа
# налево. Используйте функцию filter и сравнение строк.
poli_words = [
    "топот",
    "привет",
    "шабаш шабаш шабаш",
    "Лёша на полке клопа нашёл",
    "SOS",
    "А роза Азора",
    "Python"
]
print(poli_words)
palindrome = list(filter(lambda x: x.lower().replace(' ', '') == x[::-1].lower().replace(' ', ''), poli_words))
print(palindrome)
print()

print("lesson 8 - 10")
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества гласных букв в словах.
# Используйте функцию sorted и ключ сортировки.
print(words)
words_new = sorted(words, key=lambda x: sum([1 for i in x if i.lower() in 'аеёиоуыэюя']))
print(words_new)
print()

print("lesson 8 - 11")
# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки в верхнем регистре.
# Используйте функцию map и встроенный метод строк upper.
print(sentences)
sentences_new = list(map(lambda x: x.upper(), sentences))
print(sentences_new)
print()

print("lesson 8 - 12")
# Напишите код, который принимает список строк и возвращает новый список,
# содержащий эти же строки с добавленным префиксом “Hello”.
# Используйте функцию map и конкатенацию строк.
print(sentences)
sentences_new = list(map(lambda x: 'Hello, ' + x, sentences))
print(sentences_new)
print()

print("lesson 8 - 13")
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества букв “a” в словах.
# Используйте функцию sorted и ключ сортировки.
print(words)
words_new = sorted(words, key=lambda x: sum([1 for i in x if i.lower() == 'а']))
print(words_new)
words_new = sorted(words, key=lambda x: x.lower().count("а"))
print(words_new)
# Для закрепления - обратный порядок сортировки
words_new = sorted(words, key=lambda x: sum([1 for i in x if i.lower() == 'а']), reverse=True)
print(words_new)
words_new = sorted(words, key=lambda x: x.lower().count("а"), reverse=True)
print(words_new)
print()

print("lesson 8 - 14")
# Напишите код, который принимает список слов и возвращает новый список,
# отсортированный по возрастанию количества уникальных букв в словах.
# Используйте функцию sorted и ключ сортировки.

# Уникальные буквы — это те, которые встречаются всего один раз.

print(words)
words_new = sorted(words, key=lambda x: len(set(x.lower())))
print(words_new)
print()
