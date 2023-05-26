# Задача 1. Матрица

var_n = int(input("Введите размерность матрицы N: "))
for row in range(1, var_n + 1):
	for col in range(1, var_n + 1):
		if row % 2 == 0:
			print(row, end='\t')
		else:
			print(col, end='\t')
	print()

# Задача 2. Чёрный ящик

var_n = int(input("Введите размер матрицы: "))
for row in range(1, var_n + 1):
	for col in range(1, var_n + 1):
		if col % 3 == 0:
			print(col, end='\t')
		else:
			print(row, end='\t')
	print()

# Задача 3. Координатные оси

for row in range(20):
	for col in range(50):
		if col == 24:
			print('|', end='')
		elif row == 9:
			print('-', end='')
		else:
			print(' ', end='')
	print()
