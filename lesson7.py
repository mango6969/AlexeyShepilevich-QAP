from typing import Any, Callable, Generator

# Задание №1

"""Используя filter() и lambda, отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа."""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(filter(lambda a: a % 2 != 0, list1))
print(list2)

# Задание №2

"""Напишите функцию apply_operations(numbers, *operations), которая принимает список чисел и произвольное количество lambda-функций, последовательно применяя каждую ко всему списку."""


def apply_operations(numbers: list, *operations: Callable) -> list:
    for operation in operations:
        numbers = [operation(x) for x in numbers]
    return numbers


nums = [1, 2, 3, 4]

result = apply_operations(nums, lambda x: x * 2, lambda x: x + 3)

print(result)

# Задание №3

"""Напишите генератор chunked(lst, size), который разбивает список на куски заданного размера и поочередно их выдает. Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5]."""


def chunked(lst: list, size: int) -> Generator:
    for i in range(0, len(lst), size):
        yield lst[i : i + size]


numbers = [1, 2, 3, 4, 5]

for chunk in chunked(numbers, 2):
    print(chunk)

# Задание №4

"""Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. Выведите первые 20."""


def prime_numbers() -> Generator:
    for num in range(2, 10**9):
        is_prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num


gen = prime_numbers()

for i in range(20):
    print(next(gen))

# Задание №5

"""Напишите функцию safe_convert(value, type_func), которая пытается преобразовать value с помощью переданной функции (например, int, float). При ошибке возвращает None."""


def safe_convert(value: Any, type_func: Callable):
    try:
        return type_func(value)
    except Exception:
        return None


def convert(a: float):
    new_a = int(a)
    return new_a


result = safe_convert(2.65, convert)
print(result)
result = safe_convert("ывыв", convert)
print(result)

# Задание №6

"""Создайте собственный класс исключения NegativeNumberError. Напишите функцию sqrt_safe(n), 
которая считает квадратный корень из числа, но при отрицательном n выбрасывает NegativeNumberError с понятным сообщением."""


class NegativeNumberError(Exception):
    pass


def sqrt_safe(n: int) -> int:

    if n < 0:
        raise NegativeNumberError("n не может быть отрицательным")
    return n**0.5


try:
    print(sqrt_safe(-7))
except NegativeNumberError as e:
    print(e)

# Задание №7

"""Напишите функцию-калькулятор calculator(a, b, op), где op — строка ("+", "-", "*", "/"). 
Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов."""


def calculator(a: int | float, b: int | float, op: str) -> int | float:

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Некорректные типы аргументов")

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Нельзя делить на ноль")
        return a / b
    else:
        raise ValueError("Неизвестная операция")


try:
    result = calculator(2, 2, "*")
    print(result)
except Exception as e:
    print(e)
