# Задача 1. Конвертация.

price = float(input("Введите цену в евро: "))
rubble_price = round(price * 1.25 * 60.87, 2)
print(f"Цена в рублях: {rubble_price} рублей")

# Задача 2. Грубая математика.

import math

sum_num = int(input("Введите количество чисел: "))
for i in range(sum_num):
	num = float(input("Введите число: "))
	if num > 0:
		num = math.ceil(num)
		print(f"x = {num} log(x) = {math.log(num)}")
	else:
		num = math.floor(num)
		print(f"x = {num} exp(x) = {math.exp(num)}")

# Задача 3. Убийца Steam.

file_size = int(input("Укажите размер файла для скачивания (МБ): "))
internet_connect_speed = int(
	input("Какова скорость вашего соединения (МБ/с): "))
download_time, percent_complete = 0, 0
download_progress = 0
while file_size != download_progress:
	download_time += 1
	download_progress += internet_connect_speed
	if download_progress > file_size:
		download_progress = file_size
	percent_complete = round(download_progress / file_size * 100, 2)
	print(
		f"Прошло {download_time} сек. Скачано {download_progress} из {file_size} Мб ({percent_complete}%)")

# Задача 4. Первая цифра.

var_x = float(input("Введите вещественное число: "))
var_x = int(var_x * 10)
print(f"Первая цифра после десятичной точки: {var_x % 10}")

# Задача 5. Вот это объёмы!

import math

earth_capacity = 1.08321 * 10 ** 12
planet_radius = float(input("Введите радиус случайной планеты: "))
planet_capacity = 4 / 3 * math.pi * planet_radius ** 3
if planet_radius < 6371:
	difference = round(earth_capacity / planet_capacity, 3)
	print(f"Объём планеты Земля больше в {difference} раз")
elif planet_radius > 6371:
	difference = planet_capacity / earth_capacity
	coefficient = 1 / difference
	print(
		f"Объём планеты Земля меньше в (1/{round(coefficient, 3)}) = {round(difference, 3)} раз")
else:
	print(f"Объёмы планет равны")

# Задача 6. Ход конём.

coordinate_x, coordinate_y = 0, 0
new_coord_x, new_coord_y = 0, 0


class NewEx(Exception):
	pass


try:
	print("Введите местоположение коня:")
	coordinate_x = float(input("По горизонтали (x): "))
	coordinate_y = float(input("По вертикали (y): "))
	if coordinate_x > 0.8 or coordinate_y > 0.8 or coordinate_x < 0 or coordinate_y < 0:
		raise NewEx("Клетки с такими координатами не существуют для коня")
	coordinate_x = int(coordinate_x * 10)
	coordinate_y = int(coordinate_y * 10)

	print("Введите местоположение точки на доске:")
	new_coord_x = float(input("По горизонтали (x): "))
	new_coord_y = float(input("По вертикали (y): "))
	if new_coord_x > 0.8 or new_coord_y > 0.8 or new_coord_x < 0 or new_coord_y < 0:
		raise NewEx(
			"Клетки с такими координатами не существуют для точки на доске")
	new_coord_x = int(new_coord_x * 10)
	new_coord_y = int(new_coord_y * 10)

	print(
		f"Конь в клетке ({coordinate_x}, {coordinate_y}). Точка в клетке ({new_coord_x}, {new_coord_y})")
except NewEx:
	print("Клетки с такой координатой не существует")


def horse_move(x1, y1, x2, y2):
	dx = abs(x2 - x1)
	dy = abs(y2 - y1)
	return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)


if horse_move(coordinate_x, coordinate_y, new_coord_x, new_coord_y):
	print("Конь может сделать ход в указанную клетку")
else:
	print("Конь не может сделать ход в указанную клетку")

# Задача 7. За что?

import math

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))


def find_max(a, b):
	diff_num = a - b
	sum_num = a + b
	return (sum_num + abs(diff_num)) // 2


maximum = find_max(first_num, second_num)
print(f"Наибольшее число: {maximum}")
