# Задача 1. Таблица кубов

var_n = int(input("Введите число: "))
for i in range(2, var_n + 1, 2):
	print(f"{i} ^ 3 = {i ** 3}")

# Задача 2. Деление клетки

hour = int(input("Введите число часов: "))
cells = 1
for i in range(0, hour + 1, 3):
	print("Прошло часов:", i)
	print("Клеток:", cells)
	print("Часов до конца эксперимента:", hour - i)
	print()
	cells *= 2

# Задача 3. Квадраты нечётных чисел

var_n = int(input("Введите число: "))
for i in range(1, var_n + 1, 2):
	print(f"{i} ** 2 = {i ** 2}")
