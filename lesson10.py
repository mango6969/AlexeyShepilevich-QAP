import math
from dataclasses import dataclass

# Задание №1

"""Создай класс Circle с protected атрибутом _radius. Добавь @property для radius (с проверкой: радиус > 0),
и вычисляемые свойства area и perimeter через @property - они должны пересчитываться автоматически при изменении радиуса."""


class Circle:
    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property
    def radius(self) -> float:
        if self._radius > 0:
            return self._radius
        else:
            raise ValueError("Введите значение больше 0")

    @property
    def perimeter(self) -> float:

        return math.pi * 2 * self._radius

    @property
    def area(self) -> float:

        return math.pi * (self._radius**2)


try:
    c = Circle(5)

    print(c.radius)
    print(c.perimeter)
    print(c.area)
except Exception as e:
    print(e)


# Задание №2

"""Создай класс Vector с атрибутами x и y.
Реализуй магические методы
__add__ (сложение двух векторов),
__str__ (вывод в формате "Vector(x, y)"), и
__eq__ (сравнение).
Проверь: Vector(1, 2) + Vector(3, 4) должен давать Vector(4, 6)."""


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, a: "Vector") -> "Vector":
        return Vector(self.x + a.x, self.y + a.y)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, a: "Vector") -> bool:
        return self.x == a.x and self.y == a.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2

print(v3)
print(v1 == v3)

# Задание №3

"""Создай класс Temperature с @property для celsius, fahrenheit и kelvin. 
При установке значения через любое свойство должны автоматически пересчитываться остальные. Хранить следует только одно внутреннее значение."""


class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius1 = celsius

    @property
    def celsius(self) -> float:
        return self.celsius1

    @property
    def fahrenheit(self) -> float:
        return (self.celsius1 * 1.8) + 32

    @property
    def kelvin(self) -> float:
        return self.celsius1 + 273.15

    def set_celsius(self, value: float) -> None:
        self.celsius1 = value

    def set_fahrenheit(self, value: float) -> None:
        self.celsius1 = (value - 32) / 1.8

    def set_kelvin(self, value: float) -> None:
        self.celsius1 = value - 273.15


t = Temperature(5)

print(t.fahrenheit)

t.set_fahrenheit(50)

print(t.kelvin)

# Задание №4

"""Используй @dataclass для создания класса Point с полями x: float и y: float.
Добавь метод distance_to(other: Point) - расстояние до другой точки.
Затем создай дочерний @dataclass класс Point3D, добавив поле z: float, и переопредели distance_to."""


@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


@dataclass
class Point3D(Point):
    z: float

    def distance_to(self, other: "Point3D") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


p1 = Point(0, 0)
p2 = Point(3, 4)

print(p1.distance_to(p2))


p3 = Point3D(0, 0, 0)
p4 = Point3D(1, 2, 2)

print(p3.distance_to(p4))


# Задание №5

"""Создай класс-итератор Countdown, который при итерации возвращает числа от start до 0. 
Реализуй __iter__ и __next__ (при исчерпании бросай StopIteration). Проверь в цикле for и через list()."""


class Countdown:
    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current


for i in Countdown(10):
    print(i)


class A:
    pass
