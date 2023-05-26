# Задача 1. Герон
import math

a = int(input("Введите сторону треугольника a: "))
b = int(input("Введите сторону треугольника b: "))
c = int(input("Введите сторону треугольника c: "))
p = (a + b + c) / 2
square = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Площадь треугольника: {round(square, 2)}")

# Задача 2. Игра

distance = int(input("Введите расстояние, которое прошёл персонаж: "))
angle = int(input("Введите угол (град), под которым прошёл персонаж: "))
coord_x, coord_y = 0, 0
print(f"Текущие координаты: ({coord_x}, {coord_y})")
coord_x = distance * math.cos(angle * math.pi / 180)
coord_y = distance * math.sin(angle * math.pi / 180)
print(f"Новые координаты: ({round(coord_x, 3)},{round(coord_y, 3)})")

# Задача 3. Мега-калькулятор

number = float(input("Введите число: "))
print(f"Округление вниз: {math.floor(number)}")
print(f"Округление вверх: {math.ceil(number)}")
print(f"Модуль числа: {abs(number)}")
print(f"Квадратный корень: {math.sqrt(number)}")
print(f"Возведение экспоненты в степень числа: {math.exp(number)}")
print(f"Натуральный логарифм: {math.log(number)}")
print(f"Логарифм числа по основанию 2: {math.log2(number)}")
print(f"Логарифм числа по основанию 10: {math.log10(number)}")
print(f"Синус: {math.sin(number)}")
print(f"Косинус: {math.cos(number)}")
number = int(number)
print(f"Факториал: {math.factorial(number)}")
