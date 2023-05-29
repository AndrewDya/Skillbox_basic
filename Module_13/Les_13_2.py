# Задача 1. Сумма чисел 2


def total_n(N):
	total_num = 0
	for i in range(N + 1):
		total_num += i
	print(f"Сумма от 1 до {N} = {total_num}")
	return total_num


var_n = int(input("Введите число: "))
total_n(total_n(var_n))


# Задача 2. «Назад в будущее»

def gcd(a, b):
	if a == 0:
		return b
	if b == 0:
		return a
	while b != 0:
		a, b = b, a % b
	return a


var_a = int(input("Введите первое число: "))
var_b = int(input("Введите второе число: "))
print(f"НОД: {gcd(var_a, var_b)}")


# Задача 3. Приоритет задач

def numeral_count(N):
	long_num, count_num = 0, 0
	for i in range(1, N + 1):
		num = int(input("Введите число: "))
		if num > 0 and long_num < num:
			long_num = num
			count_num = 0
			while num > 0:
				num //= 10
				count_num += 1
	return f"Первая задачу на обработку: {long_num} длиной {count_num}"


var_n = int(input("Введите кол-во задач: "))
print(numeral_count(var_n))
