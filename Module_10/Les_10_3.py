# Задача 1. Врата

print('-' * 30)
for col in range(1, 20):
	for row in range(1, 30):
		if row == 1:
			print('|', end='')
		elif row == 29:
			print('|', end='')
		print(' ', end='')
	print()

# Задача 2. Дорога

for row in range(20):
	for col in range(50):
		if col == 24:
			print('|', end='')
		if col == row + 28:
			print('\\', end='')
		if col == -row + 19:
			print('/', end='')
		elif row == 9:
			print('-', end='')
		else:
			print(' ', end='')
	print()

# Задача 3. Диагональная матрица

var_n = int(input("Введите размер матрицы: "))
for row in range(1, var_n + 1):
	for col in range(1, var_n + 1):
		if row == var_n + 1 - col:
			print(1, end=' ')
		elif row < var_n + 1 - col:
			print(0, end=' ')
		else:
			print(2, end=' ')
	print()
