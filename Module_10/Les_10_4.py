# Задача 1. Электронная очередь

people_turn = int(input("Введите длину очереди: "))
for hour in range(people_turn + 2):
	print('Идёт час:', hour)
	for number in range(hour, people_turn + 1):
		print('Номер в очереди:', number)
	print()
print("Очередь обслужена!")

# Задача 2. Цифры больше пяти

seq_num = int(input("Сколько будет чисел: "))
count_num = 0
for i in range(1, seq_num + 1):
	num = int(input(f"Введите {i} число: "))
	while num > 0:
		res_num = num % 10
		if res_num > 5:
			count_num += 1
		num //= 10
print(f"Цифр больше 5 в {count_num} числах")

# Задача 3. Лестница чисел

var_n = int(input("Введите размер матрицы: "))
for row in range(var_n + 1):
	for col in range(var_n + 1):
		if row == var_n - col:
			print(var_n, end=' ')
		elif row < var_n - col:
			print(row + col, end=' ')
		else:
			print(" ", end=' ')
	print()
