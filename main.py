# Домашнее задание
# №1
a = 2.99
print(int(a))

b = -1.6
print(int(b))

# №2
link = "www.my_site.com#about"
new_link = link.replace("#", "/")
print(new_link)

# №3
stroka_ing = "stroka" + "ing"
print(stroka_ing)

# №4
text = "Ivanou Ivan"
a1, a2 = text.split()
result = f"{a2} {a1}"
print(result)

# №5
str1 = "   Delete   "
print(str1.strip())

# №6
school = {
    "1а": 10,
    "1б": 7,
    "1в": 20,
    "6б": 13,
    "9г": 25,
    "8а": 9,
    "7в": 16,
    "3д": 14,
    "4б": 18,
    "7а": 19,
}
print(school)

# №7
list1 = [1, 2, 3]
print(list1[1])

# №8
s1 = "employ"
s2 = "employment"
print(s1 in s2)

# №9
x = "My name is Agent Smith"
print(x[1])  # y
print(x[3:16:3])  # nesgt

# №10
numbers = [1, 5, 2, 9, 2, 9, 1]
for num in numbers:
    if numbers.count(num) == 1:
        print(num)
