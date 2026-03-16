# Задание №1

a = int(input())
result = a + 1 if a > 0 else a
print(result)

# Задание №2

my_list = [-1, 2, 3]
count = 0
for i in my_list:
    if i > 0:
        count += 1
print(count)

# Задание №3

year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("366")
        else:
            print("365")
    else:
        print("366")
else:
    print("365")

# Задание №4

a = int(input())
b = int(input())

total = 0

for i in range(a, b + 1):
    total += i

print(total)

# Задание №5

numbers = [int(input()) for i in range(10)]
umn = 1
summa = 0
count1 = 0

for i in numbers:
    if i > 0:
        umn *= i
    else:
        summa += i
        count1 += 1
print("Произведение положительных:", umn)
print("Сумма отрицательных:", summa)
print("Кол-во отрицательных:", count1)

# Задание №6

n = 10
result1 = 1

for i in range(1, n + 1):
    result1 *= i
print(f"Произведение: {result1}")

# Задание №7

s1 = int(input())
s2 = int(input())

years = 0

while s1 >= 0.1 * s2:
    s1 *= 2
    s2 *= 3
    years += 1

print(years)

# Задание №8

n = int(input())

while n != 1:
    digits = [int(i) for i in str(n)]
    n = sum(d**2 for d in digits)

if n == 1:
    print(True)
else:
    print(False)
