def square(a: int) -> int:
    return a**2


def cube(a: int) -> int:
    return a**3


def is_even(a: int | float) -> bool:
    return a % 2 == 0


if __name__ == "__main__":
    print(square(2))
    print(cube(2))
    print(is_even(3))
