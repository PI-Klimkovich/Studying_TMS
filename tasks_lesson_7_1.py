# Напишите функцию make_sentence, которая принимает один именованный
# аргумент words, который должен быть списком строк, и возвращает строку,
# составленную из элементов списка, разделенных пробелами и
# заканчивающуюся точкой. Если аргумент words не указан, то по умолчанию
# используется список ["This", "is", "a", "sentence"].

def make_sentence(words=None):
    """
    Из списка преобразуется в строку через пробелы
    :param words: list
    :return: str
    """
    if words is None:
        words = ["This", "is", "a", "sentence"]
    return ' '.join(words) + '.'


print("lesson 7 - 1")
text = """Напишите функцию, которая принимает один именованный аргумент, 
который должен быть списком строк, и возвращает строку, 
составленную из элементов списка, разделенных пробелами 
и заканчивающуюся точкой"""
tett_list = text.split()
print(tett_list)
print(make_sentence(tett_list))
print(make_sentence())
print()


# Напишите функцию sum_of_squares, которая принимает произвольное
# количество позиционных аргументов, которые должны быть числами,
# и возвращает сумму их квадратов. Если функции не передано ни одного
# аргумента, она должна вернуть 0.

def sum_of_squares(*args: int | float):
    """
    Сумма квадратов переданных чисел
    :param args: произвольное количество чисел
    :return: число
    """
    total = 0
    for i in args:
        total += i ** 2
    return total


print("lesson 7 - 2")
print(sum_of_squares(1, 2, 4, 66.2))
print(sum_of_squares(1, 2, 3, 4))
print(sum_of_squares())
print()

# Напишите функцию greet, которая принимает два именованных аргумента:
# name и language. Аргумент name должен быть строкой, а аргумент language
# должен быть одним из трех возможных значений: "en", "ru" или "fr".
# Функция должна возвращать приветствие на выбранном языке.
# Если аргумент language не указан, то по умолчанию используется "en".


def greet(name: str, language="en"):
    """
    Приветствие на выбранном языке:
    "en", "ru" или "fr"
    :param name: Имя
    :param language: "en", "ru" или "fr"
    """
    if language == "en":
        return f"Helo, {name}!"
    elif language == "ru":
        return f"Привет, {name}!"
    else:
        return f"Bonjour, {name}!"


print("lesson 7 - 3")
print(greet('Pol'))
print(greet("Алинушка", 'ru'))
print()

# Напишите функцию print_info, которая принимает произвольное
# количество именованных аргументов (**kwargs) и выводит их в формате
# "key: value" по одной паре на строку. Напоминаю, что kwargs в функции
# будет словарем. Если функции не передано ни одного аргумента, она должна
# вывести "No info given.".


def print_info(**kwargs):
    """
    Обработка произвольного количества именованных аргументов
    :param kwargs: Произвольные именованные аргументы
    :return: вывод в виде словаря
    """
    if len(kwargs) == 0:
        print("No info given.")
        return
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("lesson 7 - 4")
print()
print_info(name="Alex", age=25, city="Amsterdam")
print()
print_info(name="Алинушка", language='ru')
print()
print_info()
print()


# Напишите функцию print_table, которая принимает произвольное
# количество именованных аргументов в виде пар ключ-значение и выводит их
# в виде таблицы с двумя столбцами: "Key" и "Value". Если функции не
# передано ни одного аргумента, она должна вывести "No data given.".


def print_table(**kwargs):
    """
    Обработка произвольного количества именованных аргументов и выводит в виде таблицы
    :param kwargs: Произвольные именованные аргументы
    :return: вывод в виде таблицы
    """
    if len(kwargs) == 0:
        print("No info given.")
        return
    len_key = max(len(key) for key, value in kwargs.items())
    if len_key < 3:
        len_key = 3
    len_value = max(len(str(value)) for key, value in kwargs.items())
    if len_value < 5:
        len_value = 5
    print("| Key" + (len_key - 2) * ' ' + "| Value" + (len_value - 4) * ' ' + '|')
    print('|' + (len_key + 2) * '-' + '|' + (len_value + 2) * '-' + '|')
    for key, value in kwargs.items():
        print(f"| {key}{(len_key - len(key)) * ' '} | {value}{(len_value - len(str(value))) * ' '} |")


def print_table_new(**kwargs):
    """
    Обработка произвольного количества именованных аргументов и выводит в виде таблицы
    :param kwargs: Произвольные именованные аргументы
    :return: вывод в виде таблицы
    """
    if len(kwargs) == 0:
        print("No info given.")
        return
    len_key = max(len(key) for key, value in kwargs.items())
    if len_key < 3:
        len_key = 3
    len_value = max(len(str(value)) for key, value in kwargs.items())
    if len_value < 5:
        len_value = 5
    print("| Key" + (len_key - 2) * ' ' + "| Value" + (len_value - 4) * ' ' + '|')
    print('|' + (len_key + 2) * '-' + '|' + (len_value + 2) * '-' + '|')
    for key, value in kwargs.items():
        print(f"| {key}{(len_key - len(key)) * ' '} | {value:<{len_value}} |")


print("lesson 7 - 5")
print_table(name="Bob", age=30, city="Amsterdam")
print()
print_table(name="Алинушка", language='by')
print()
print_table()
print()
print_table(nu="пр", va='ru')
print()
print_table(name="Alex", age=25, city="Amsterdam", language='ru')
print()

print_table_new(name="Bob", age=30, city="Amsterdam")
print()
print_table_new(name="Алинушка", language='by')
print()
print_table_new()
print()
print_table_new(nu="пр", va='ru')
print()
print_table_new(name="Alex", age=25, city="Amsterdam", language='ru')
print()


# Напишите функцию calculate, которая принимает произвольное количество
# позиционных аргументов, которые должны быть числами, и один
# именованный аргумент operation, который должен быть одним из четырех
# возможных значений: "+", "-", "*" или "/".
# Функция должна возвращать результат выполнения указанной операции над
# всеми числами в порядке их передачи.
# Если функции не передано ни одного позиционного аргумента, она должна вернуть 0.
# Если аргумент operation не указан, то по умолчанию используется "+".
# Пример вызова: calculate(1, 2, 3, operation="*")


def calculate(*args: int | float, operation=None):
    """
    Калькулятор ограниченного функционала.
    Переданное действие распространяется на все входной массив чисел
    :param args: Числа
    :param operation: "+", "-", "*" или "/"
    :return: Число либо "деление на ноль*
    """
    res = 0
    if len(args) > 0:
        if operation is None:
            operation = "+"
        if operation == '+':
            for number in args:
                res += number
        elif operation == '-':
            for number in args:
                res -= number
        elif operation == '*':
            res = 1
            for number in args:
                res *= number
        elif operation == '/':
            res = args[0]
            for i in range(1, len(args) - 1):
                if args[i] == 0:
                    res = "Деление на ноль!"
                    break
                res /= args[i]
    return res


print("lesson 7 - 6")
print(calculate(1, 3, 9, 8.8, operation="+"))
print()
print(calculate(1, 3, 9, 8.8, operation="*"))
print()
print(calculate(1, 3, 9, 8.8, operation="-"))
print()
print(calculate(1, 3, 9, 8.8, operation="/"))
print()
print(calculate(0, 3, 9, 8.8, operation="/"))
print()
print(calculate(1, 3, 0, 8.8, operation="/"))
print()
print(calculate(8, 9, 7, 14))
print()
print(calculate(2))
print()
print(calculate())
print()
print(calculate(operation="/"))
print()


# Напишите функцию print_triangle, которая принимает один именованный
# аргумент height, который должен быть положительным целым числом, и
# выводит равнобедренный треугольник из символов "*" с заданной высотой.
# Если аргумент height не указан, то по умолчанию используется число 5.


def print_triangle(height=None):
    """
    Построение треугольника по его высоте
    :param height: высота - целое число
    """
    if height is None:
        height = 5
    for i in range(height):
        print((height - i - 1) * ' ' + (2 * i + 1) * '*')


print("lesson 7 - 7")
print_triangle(2)
print_triangle(6)
print_triangle(15)
print_triangle()

# Напишите функцию create_post, которая создает пост для блога,
# основываясь на переданных параметрах. Обязательными параметрами
# являются: заголовок, содержимое и автор. Необязательным параметром
# является категория. Если она не была передана, то по умолчанию будет
# текущая значение “general”. Функция должна возвращать словарь поста.


def create_post_chaos(**kwargs):
    """
    Создание словаря поста. не упорядоченны
    :param kwargs: Структура и содержимое поста
    :return: Хаотичный вывод содержимого словаря
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    if kwargs.get('category') is None:
        kwargs['category'] = 'general'
        print('category:', kwargs['category'])


def create_post_bed(**kwargs):
    post_dict = {}
    post_dict['titl'] = kwargs['titl']
    post_dict['text'] = kwargs['text']
    post_dict['autor'] = kwargs['autor']
    if kwargs.get('category') is None:
        post_dict['category'] = 'general'
    else:
        post_dict['category'] = kwargs['category']
    return post_dict


def create_post(titul: str, text: str, autor: str, category=None):
    post_dict = {
        'titul': titul,
        'text': text,
        'autor': autor,
    }
    if category is None:
        post_dict['category'] = 'general'
    else:
        post_dict['category'] = category
    return post_dict


print("lesson 7 - 8")
create_post_chaos(titl='Заголовок', text="некий много насыщенный текст.", autor='Helen', category='in said')
print()
create_post_chaos(titl='Заголовок', text="некий вовсе не насыщенный текст.", autor='Helen')
print()
create_post_chaos(text="некий насыщенный текст.", category='out said', titl='Заголовок', autor='Helen')
print()

print(create_post_bed(titl='Заголовок', text="некий многонасыщенный текст.", autor='Helen', category='in said'))
print()
print(create_post_bed(titl='Заголовок', text="некий многонасыщенный текст.", autor='Helen'))
print()
print(create_post_bed(text="некий насыщенный текст.", category='out said', titl='Заголовок', autor='Helen'))
print()

print(create_post(titul='Заголовок', text="некий многонасыщенный текст.", autor='Helen', category='in said'))
print()
print(create_post(titul='Заголовок', text="некий многонасыщенный текст.", autor='Helen'))
print()
print(create_post(text="некий насыщенный текст.", category='out said', titul='Заголовок', autor='Helen'))
print()


# Напишите функцию create_product, которая создает товар для интернет-
# магазина, основываясь на переданных параметрах. Обязательными
# параметрами являются: имя, цена и категория. Необязательным параметром
# является рейтинг. Если он не был передан параметр, то по умолчанию будет
# 0. Функция должна возвращать словарь товара.


def create_product(name: str, price: int | float, category: str, rating=None):
    product_dict = {
        'name': name,
        'price': price,
        'category': category
    }
    if rating is None:
        product_dict['rating'] = 0
    else:
        product_dict['rating'] = rating
    return product_dict


print("lesson 7 - 9")
print(create_product(name='Заголовок', price=12.50, category='in said', rating=6))
print()
print(create_product(name='Заголовок', price=44.88, category='Helen'))
print()
print(create_product(price=52, category='out said', name='Заголовок', rating=16))
print()


# Напишите функцию create_student, которая создает словарь студента
# для учебного заведения, основываясь на переданных параметрах.
# Обязательными параметрами являются: имя, фамилия, отчество и группа.
# Также дополнительными параметрами могут быть: дата поступления в виде
# строки «19.10.2023», средний бал, семестр обучения, номер телефона, адрес.
# Функция должна возвращать словарь студента только с переданными
# данными, если некоторые данные не были переданы, то их не должно быть в словаре.


def create_student(name, surname, middle_name, group, **kwargs):
    person = {
        'name': name,
        'surname': surname,
        'middle_name': middle_name,
        'group': group,
    }
    person.update(kwargs)
    return person


print("lesson 7 - 10")
print(create_student(name='Pol', surname='Petrov', middle_name='Petrovich', group="Py45-onl"))
print()
print(create_student(name='Max', surname='Sidorovka', middle_name='Faktor', group="Py45-onl",
                     data_com='19.10.2023', average_mark=7.56, semester=3,
                     phone_number='+37566 4445522', address='Minskas'))
print()
print(create_student(name='Roma', surname='Volov', middle_name='Sergeevich', group="Py42-onl",
                     data_com='11.11.2020', average_mark=8.88, semester=5,
                     phone_number='+37533 2223344', address='Pinskas'))
print()
print(create_student(name='Serg', surname='Nekiy', middle_name='Ivanovich', group="Py4-onl",
                     data_com='01.01.2010', average_mark=9.08, phone_number='+37522 3334455'))
print()
