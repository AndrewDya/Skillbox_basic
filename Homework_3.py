# Задача 1
a, b, c, d = 8, 10, 12, 18
res = ((-3 + a ** 2) * 2 - 2 ** 3) / (c - 2 * d)
print(res)

# Задача 2
first_quarter = int(input("Введите доход первого квартала: "))
second_quarter = int(input("Введите доход второго квартала: "))
third_quarter = int(input("Введите доход третьего квартала: "))
fourth_quarter = int(input("Введите доход четвёртого квартала: "))
first_half = first_quarter + second_quarter
second_half = third_quarter + fourth_quarter
trend = first_half / second_half
print(trend)

# Задача 3
number = int(input("Введите число: "))
print(f"После числа {number} идёт число {number + 1}")
print(f"До числа {number} идёт число {number - 1}")

# Задача 4
first_side = int(input("Введите длину 1-ого катета: "))
second_side = int(input("Введите длину 2-ого катета: "))
square = first_side * second_side / 2
print(f"Площадь треугольника: {square}")

# Задача 5
minutes = int(input("Введите значение: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} минут - это {hours} часа и {remaining_minutes} минут")

# Задача 6
first_num = int(input("Введите 1-ое число: "))
second_num = int(input("Введите 2-ое число: "))
total = first_num % 100 + second_num % 100
print("Cумма", total)

# Задача 7
num = int(input("Введите 4-ёх значное число: "))
print(num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10)

# # Задача 8
# Напишите программу, которая меняла бы значения двух переменных местами, но без использования
# третьей переменной и синтаксического сахара, который мы разбирали, а именно: без конструкции a, b = b, a.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)
