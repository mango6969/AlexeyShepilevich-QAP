def square(a: int) -> int:
    return a**2


def cube(a: int) -> int:
    return a**3


def is_even(a: int | float) -> bool:
    return a % 2 == 0


def mean(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def variance(numbers: list[float]) -> float:
    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers)


def standard_deviation(numbers: list[float]) -> float:
    return variance(numbers) ** 0.5


if __name__ == "__main__":
    print(square(2))
    print(cube(2))
    print(is_even(3))
