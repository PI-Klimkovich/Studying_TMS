print("lesson 8 - 15")
# ННапишите декоратор retry_five, который повторяет вызов декорируемой функции 5 раз.


def retry_five(func):
    """
    Декоратор принимает любую функцию и повторяет вызов декорируемой функции 5 раз.
    :param func: (Функция), которую надо декорировать.
    :return: (Функция) Декоратор для переданной функции.
    """

    def wrapper(*args, **kwargs):
        print()
        print(f"Первый вызов функции")
        func(*args, **kwargs)
        print(f"Второй вызов функции")
        func(*args, **kwargs)
        print(f"Третий вызов функции")
        func(*args, **kwargs)
        print(f"Четвертый вызов функции")
        func(*args, **kwargs)
        print(f"Пятый вызов функции")
        res = func(*args, **kwargs)
        print(f"--------- end ---------")
        return res

    return wrapper


@retry_five
def squaring_numbers(numbers: list[int | float]) -> list[int | float]:
    new_numbers = []
    for number in numbers:
        new_numbers.append(number ** 2)
    return new_numbers


@retry_five
def words_in_sentence(words: list[str]) -> None:
    sentence = ''
    for word in words:
        sentence += word + ' '
    print(sentence)


numbers = [1, 2, 14.43, -234, 0, -2.23, 4, 1]
words = ["шабаш", "шабаш", "шабаш"]
words_1 = ["Правильно", "ли", "я", "понял", "задание"]

print(squaring_numbers(numbers))
words_in_sentence(words)
words_in_sentence(words_1)
