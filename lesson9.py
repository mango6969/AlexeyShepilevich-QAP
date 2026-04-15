# Задание №1

"""1. Создай класс Library с атрибутом класса books = [] и методами add_book(title), remove_book(title) и show_books(). Продемонстрируй, что список книг общий для всех объектов класса."""


class Library:
    books = ["Мама", "Папа", "Я"]

    def add_book(self, title: str) -> None:
        Library.books.append(title)

    def remove_book(self, title: str) -> None:
        Library.books.remove(title)

    def show_books(self) -> list:
        return Library.books


obj = Library()

obj.add_book("Семья")
obj.remove_book("Папа")
print(obj.show_books())


# Задание №2
"""Создай иерархию: базовый класс Employee с атрибутами name и salary, методом get_info().
Дочерние классы Manager (добавляет department) и Developer (добавляет language). Каждый переопределяет get_info()."""


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def get_info(self) -> tuple:
        return self.name, self.salary


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_info(self) -> str:
        return f"Manager: {self.name}, Salary: {self.salary}, Department: {self.department}"


class Developer(Employee):
    def __init__(self, name: str, salary: float, language: str):
        super().__init__(name, salary)
        self.language = language

    def get_info(self) -> str:
        return (
            f"Developer: {self.name}, Salary: {self.salary}, Language: {self.language}"
        )


obg1 = Manager("Andrew", 100, "PM")
obj2 = Developer("Oleg", 120, "Python")

print(obg1.get_info())
print(obj2.get_info())


# Задание №3

"""Реализуй класс Stack (стек) с протектед атрибутом _items = [] и методами push(item), pop(), peek() (посмотреть верхний элемент), is_empty() и size()."""


class Stack:
    def __init__(self, items: list) -> None:
        self._items = items

    def push(self, item: str) -> None:
        self._items.append(item)

    def pop(self) -> str:
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> str:
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


obj = Stack([7, 4, 5, 9, 6, 3])

obj.push(1)
print(obj.pop())
print(obj.peek())
print(obj.is_empty())
print(obj.size())


# Задание №4


"""Создай класс Vehicle с методом move(), выводящим "Moving...". Создай дочерние классы Car, Boat и Plane, каждый переопределяет move() по-своему.
Напиши функцию start_journey(vehicle), которая вызывает move() у любого переданного транспорта - продемонстрируй полиморфизм."""


class Vehicle:
    def move(self) -> None:
        print("Moving...")


class Car(Vehicle):
    def move(self) -> None:
        print("Moving car")


class Boat(Vehicle):
    def move(self) -> None:
        print("Moving boat")


class Plane(Vehicle):
    def move(self) -> None:
        print("Moving plane")


def start_journey(vehicle: Vehicle) -> None:
    vehicle.move()


obj1 = Car()
obj2 = Boat()
obj3 = Plane()


start_journey(obj1)
start_journey(obj2)
start_journey(obj3)


# Задание №5

"""5. Создай класс Student с атрибутами name и grades (список оценок).
Добавь методы add_grade(grade), average() (средняя оценка), highest() и lowest(). Защити grades через одиночное подчёркивание."""


class Student:
    def __init__(self, name: str, grades: list) -> None:
        self.name = name
        self._grades = grades

    def add_grade(self, grade: int) -> None:
        self._grades.append(grade)

    def average(self) -> float:
        average = sum(self._grades) / len(self._grades)

        return average

    def highest(self) -> int:
        maximum = max(self._grades)

        return maximum

    def lowest(self) -> int:
        minimum = min(self._grades)

        return minimum


obj = Student("Alex", [2, 5, 3])

obj.add_grade(7)
print("Средняя:", obj.average())
print("Максимум:", obj.highest())
print("Минимум:", obj.lowest())
