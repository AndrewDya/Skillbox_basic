# Задача 1. Доска

for i in range(1, 11):
	print("-", end='')
print()
for j in range(1, 5):
	print("|", end='')
	for i in range(1, 9):
		print("0", end='')
	print("|")
for k in range(1, 11):
	print("-", end='')

# Задача 2. Локальная сеть

number = int(input("Введите число: "))
difference = int(input("Введите шаг: "))
sum_number = 0
print("\nIP-adress:", end=' ')
for i in range(1, 4):
	print(number, end='.')
	sum_number += number
	number += difference
print(sum_number)

# Задача 3. Табло

number_n = int(input("Введите число: "))
for i in range(0, number_n + 1, 10):
	print("-=-", i, end=' ')
print("-=-")
