import warnings
from functools import wraps
from typing import Any, Callable

# Задание №1

"""Напишите рекурсивную функцию palindrome(s), которая проверяет, является ли строка палиндромом. Без срезов и reversed(), только рекурсия."""


def palindrome(s: str, left: int = 0, right: int = None) -> bool:
    if right is None:
        right = len(s) - 1

    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return palindrome(s, left + 1, right - 1)


print(palindrome("дед"))


# Задание №2

"""Напишите функцию make_validator(min_val, max_val), которая возвращает функцию-валидатор. Валидатор принимает число и возвращает True если оно в диапазоне, иначе False."""


def make_validator(min_val: float, max_val: float) -> Callable:
    def validator(x: float) -> bool:
        return min_val <= x <= max_val

    return validator


obj = make_validator(1, 10)

print(obj(5))

# Задание №3

"""Напишите декоратор @retry(n), который при возникновении любого исключения повторяет вызов функции до n раз. Если все попытки провалились — пробрасывает последнее исключение."""


def retry(n: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None

            for i in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e

            raise last_exception

        return wrapper

    return decorator


@retry(3)
def func(x: float, y: float) -> float:
    return x + y


try:
    print(func(4, "выц"))
except Exception as e:
    print(e)

# Задание №4

"""Напишите декоратор @deprecated(message), который выводит предупреждение при вызове функции (через warnings.warn) и всё равно выполняет её. Сохраняйте метаданные через functools.wraps."""


def deprecated(message: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(message, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@deprecated("Используй новую функцию new_func()")
def old_func(x: float, y: float) -> float:
    return x + y


print(old_func(2, 3))

# Задание №5

"""Напишите рекурсивную функцию binary_search(lst, target) (бинарный поиск числа в списке), оберните её декоратором @logger, который логирует каждый вызов с параметрами."""


def logger(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Вызов: {func.__name__}, args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


@logger
def binary_search(lst: list, target: int, left: int = 0, right: int = None) -> int:
    if right is None:
        right = len(lst) - 1

    if left > right:
        return -1  # не найдено

    mid = (left + right) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, left, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, right)


lst = [1, 3, 5, 7, 9, 11]

print(binary_search(lst, 7))
