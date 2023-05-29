# Задача 1. Вода

def about_water(price):
	print("Название: КлирВотер")
	print("Производитель: ВодЗавод")
	print(f"Цена: {price}")


about_water(25)
about_water(30)
about_water(40)

# Задача 2. Вот это объёмы 2

import math


def sphereArea(R):
	square = round(4 * math.pi * R * R, 2)
	print(f"Площадь сферы: {square}")


def sphereVolume(R):
	volume = round(4 / 3 * math.pi * R ** 3, 2)
	print(f"Объём сферы: {volume}")


radius = float(input("Введите радиус: "))
sphereArea(radius)
sphereVolume(radius)

# Задача 3. Простые числа

import math


def is_prime(N):
	if N < 2:
		return False
	for i in range(2, int(math.sqrt(N)) + 1):
		if N % i == 0:
			return False
	return True


var_n = int(input("Введите число N: "))
if is_prime(var_n):
	print("Число является простым.")
else:
	print("Число не является простым.")
