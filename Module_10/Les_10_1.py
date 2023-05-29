# Задача 1. Таблица умножения

for row in range(1, 10):
	for col in range(1, 10):
		print(row * col, end='\t')
	print()

# Задача 2. Таблица суммы

var_n = int(input("Введите число N: "))
for row in range(var_n + 1):
	for col in range(var_n + 1):
		print(row + col, end='\t')
	print()

# Задача 3. Анализ данных

for row in range(10):
	for col in range(0, -10, -1):
		print(row + col, end='\t')
	print()
