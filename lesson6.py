from collections.abc import Callable
from datetime import datetime

from file_utils import count_words, read_lines, write_lines

# Задание №1


"""1. Напиши функцию copy_file(source: str, destination: str) -> bool
которая читает содержимое файла source и записывает его в destination. Возвращает True если успешно. Проверь что файл-копия создался."""


def copy_file(source: str, destination: str) -> bool:
    try:
        with open(source, "r") as file1:
            content = file1.read()

        with open(destination, "w") as file2:
            file2.write(content)

        return True
    except Exception as e:
        print("Error:", e)
        return False


copy_file("source.txt", "destination.txt")

# Задание №2

"""2. Создай файл grades.txt где каждая строка содержит имя студента и его оценку через запятую:
Анна,85
Иван,72
Петр,91
Напиши код который читает файл и добавляет в конец каждой строки статус: 'отлично' если оценка >= 90, 'хорошо' если >= 75, иначе 'удовлетворительно'. 
Сохрани результат в новый файл grades_with_status.txt."""


def add_status_to_grades(source: str, destination: str) -> None:

    with open(source, "r", encoding="utf-8") as file1:
        lines = file1.readlines()

    with open(destination, "w", encoding="utf-8") as file2:
        for line in lines:
            name, grade_str = line.strip().split(",")
            grade = int(grade_str)

            if grade >= 90:
                status = "отлично"
            elif grade >= 75:
                status = "хорошо"
            else:
                status = "удовлетворительно"

            file2.write(f"{name},{grade},{status}\n")


add_status_to_grades("grades.txt", "grades_with_status.txt")

# Задание №3

"""3. Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет. """


def age_calculator(birth_date_str: str) -> int:
    birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
    today = datetime.today()

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


print(age_calculator("29/01/2001"))

# Задание №4

"""Напиши модуль file_utils.py с тремя полностью аннотированными функциями:

def read_lines(filename): ...
def write_lines(filename, lines): ...
def count_words(filename): ... 
#count_words считает сколько раз каждое слово встречается в файле и возвращает словарь. 
В main.py импортируй и протестируй все три."""


lines = read_lines("text.txt")
print("Содержимое файла:")
print(lines)


write_lines("copy.txt", lines)


words = count_words("text.txt")
print("Подсчёт слов:")
print(words)

# Задание №5

"""Напиши функцию password_checker(correct_password) которая возвращает вложенную функцию check(password). Вложенная принимает пароль и возвращает True если совпадает, иначе False."""


def password_checker(correct_password: str) -> Callable:
    def check(password: str) -> bool:
        return password == correct_password

    return check


print(password_checker("12345Qwe")("12345Qwe"))
print(password_checker("12345Qwe")("54321ewQ"))
