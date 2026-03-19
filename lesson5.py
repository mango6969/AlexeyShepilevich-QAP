import math_utils

# Задание №1
n = int(input("Введите число:"))


def table(n: int) -> None:
    for i in range(1, 10):
        result = i * n
        print(result, end="|")


table(n)

# Задание №2

name = str(input("Введите имя:"))
age = int(input("Введите возраст:"))
print(f"Через 10 лет тебе будет: {age + 10} лет, {name}")

# Задание №3


items = ["хлеб", "молоко", "кофе"]
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2


def shop(price: float) -> float:
    return price * rate


new_price = list(map(shop, prices_usd))
print(dict(zip(items, new_price)))


# Задание №4


def fizzbuzz(n: int) -> str:

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    else:
        return str(n)


result = list(map(fizzbuzz, range(1, 21)))
print(result)

# Задание №5


def my_stats(*args: int) -> tuple:
    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)

    return minimum, maximum, average


result = my_stats(1, 2, 3)
print(result)

# Задание №6


def build_profile(**kwargs: dict) -> dict:
    """
    Функция build_profile(**kwargs) принимает любые именованные аргументы и
    возвращает словарь с этими данными плюс автоматически добавляет ключ 'registered': True

    """

    profile = dict(kwargs)
    profile["registered"] = True

    return profile


user = build_profile(name="Alex", age=25)
print(user)

# Задание №7

a = int(input("Введите число:"))

print("Число в квадрате:", math_utils.square(a))
print("Число в кубе:", math_utils.cube(a))
print("Четное/нечетное:", math_utils.is_even(a))
