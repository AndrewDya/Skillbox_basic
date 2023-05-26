# # Задание 1. Тестовое задание.
#
# matrix_size = int(input("Введите размерность матрицы: "))
# step = 0
# for row in range(matrix_size):
# 	for col in range(matrix_size):
# 		print(col * 2 + step, end='\t')
# 	print()
# 	step += 1
#
# # Задание 2. Лестница.
#
# matrix_size = int(input("Введите размерность матрицы: "))
# for row in range(1, matrix_size + 1):
# 	for col in range(1, matrix_size + 1):
# 		if col == row:
# 			print(row, end=' ')
# 		elif col > row:
# 			print(" ", end=' ')
# 		elif col < row:
# 			print(row, end=' ')
# 	print()
#
# # Задание 3. Рамка.
#
# width = int(input("Введите ширину рамки: "))
# height = int(input("Введите длину рамки: "))
#
# for row in range(1, height + 1):
# 	for col in range(1, width + 1):
# 		if col == 1:
# 			print("|", end=' ')
# 		elif col == width:
# 			print("|", end=' ')
# 		elif row == 1:
# 			print("-", end=' ')
# 		elif row == height:
# 			print("-", end=' ')
# 		else:
# 			print(" ", end=' ')
# 	print()
#
# # Задание 4. Простые числа.
#
# sum_num = int(input("Введите количество чисел: "))
# sum_simple_num = 0
#
# for i in range(1, sum_num + 1):
# 	num = int(input(f"Введите {i}-ое число: "))
# 	if num < 2:
# 		continue
# 	is_prime = True
# 	for j in range(2, int(num ** 0.5) + 1):
# 		if num % j == 0:
# 			is_prime = False
# 			break
# 	if is_prime:
# 		sum_simple_num += 1
#
# print("Количество простых чисел в последовательности:", sum_simple_num)
#
# # Задание 5. Наибольшая сумма цифр.
#
# sum_num = int(input("Введите количество чисел: "))
# max_sum_digits, max_num = 0, 0
# for i in range(1, sum_num + 1):
# 	num = int(input(f"Введите {i} число: "))
# 	work_num = num
# 	sum_digits = 0
# 	while work_num > 0:
# 		remainder_num = work_num % 10
# 		work_num //= 10
# 		sum_digits += remainder_num
# 	if sum_digits > max_sum_digits:
# 		max_sum_digits = sum_digits
# 		max_num = num
# print(f"В числе {max_num}, сумма цифр больше всего: ({max_sum_digits})")
#
# # Задание 6. Пирамидка.
#
# height = int(input("Введите высоту треугольника: "))
# width = height * 2 - 1
#
# for row in range(height):
# 	for col in range(width):
# 		if height - 1 - row <= col <= height - 1 + row:
# 			print("#", end='')
# 		else:
# 			print(" ", end='')
# 	print()

# Задание 7. Пирамидка-2.

height = int(input("Введите количество уровней пирамиды: "))
width = height * 2 - 1
odd_number = 1

for row in range(height):
	for col in range(width):
		if col == height - 1 - row or col == height - 1 + row or (
				height - row <= col <= height + row and col % 2 == row % 2):
			print(odd_number, end='\t')
			odd_number += 2
		else:
			print(" ", end='\t')
	print()

# Исходный вариант
# height = int(input("Введите количество уровней пирамиды: "))
# width = height * 2 - 1
# odd_number = 1
#
# for row in range(height):
# 	for col in range(width):
# 		if height - 1 - row == col:
# 			print(odd_number, end='\t')
# 			odd_number += 2
# 		elif col == height - 1 + row:
# 			print(odd_number, end='\t')
# 			odd_number += 2
# 		elif height - 1 - row <= col <= height - 1 + row and (
# 				col % 2 == 0 and row % 2 == 0):
# 			print(odd_number, end='\t')
# 			odd_number += 2
# 		elif height - 1 - row <= col <= height - 1 + row and (
# 				row >= 3 and row % 2 == 1 and col % 2 == 1):
# 			print(odd_number, end='\t')
# 			odd_number += 2
# 		else:
# 			print(" ", end='\t')
# 	print()

# Задание 8. Яма.

# height = int(input("Введите высоту ямы: "))
# width = height * 2
# if height < 10:
# 	for row in range(1, height + 1):
# 		for col in range(1, width + 1):
# 			if col >= height + row - height + 1 and row - height <= height - col:
# 				print(".", end='')
# 			elif col - 1 < width // 2:
# 				print(height - col + 1, end='')
# 			else:
# 				print(- 1 * (height - col), end='')
# 		print()
#
# else:
# 	for row in range(1, height + 1):
# 		for col in range(1, width + 1):
# 			if col >= height + row - height + 1 and row - height <= height - col:
# 				print(".", end='\t')
# 			elif col - 1 < width // 2:
# 				print(height - col + 1, end='\t')
# 			else:
# 				print(- 1 * (height - col), end='\t')
# 		print()
