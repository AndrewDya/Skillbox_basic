# Задача 1. Урок информатики 2.

import math

var_x = float(input("Введите число: "))
degree = 0
if var_x >= 1:
	while var_x > 10:
		var_x /= 10
		degree += 1
elif 0 < var_x < 1:
	while var_x < 1:
		var_x *= 10
		degree -= 1
else:
	print("Введите положительное число")

print(
	f"Формат плавающей точки: x = {var_x:.5f} * 10 ** {degree}")


# Задача 2. Функция максимума.


def maximum_of_two(a, b):
	max_num = a if a > b else b
	return max_num


def maximum_of_three(a, b, c):
	max_num = maximum_of_two(var_a, var_b)
	max_num = maximum_of_two(max_num, var_c)
	return max_num


var_a = int(input("Введите число a: "))
var_b = int(input("Введите число b: "))
var_c = int(input("Введите число c: "))

print(f"Максимальное число из трёх: {maximum_of_three(var_a, var_b, var_c)}")


# Задача 3. Число наоборот 2.

def reverse_num(n):
	str_num = ''
	while n > 0:
		tmp = n % 10
		str_num += str(tmp)
		n //= 10
	return int(str_num)


var_n = int(input("Введите первое число: "))
var_k = int(input("Введите второе число: "))
print(f"Сумма: {var_k + var_n}")

print(f"\nПервое число наоборот: {reverse_num(var_n)}")
print(f"Второе число наоборот: {reverse_num(var_k)}")
print(f"Сумма: {reverse_num(var_n) + reverse_num(var_k)}")


# Задача 4. Недоделка 2.


def main():
	first_n = int(input("Введите первое число: "))
	second_n = int(input("Введите второе число: "))
	if first_n < 100:
		print("В первом числе меньше трёх цифр.")
	elif second_n < 1000:
		print("Во втором числе меньше четырёх цифр.")
	else:
		print(
			f"Кол-во цифр в первом числе: {count_numbers(first_n)}. Кол-во цифр во втором числе: {count_numbers(second_n)}")
		print(
			f"Первое изменённое число: {change_number(first_n, count_numbers(first_n))}. Второе изменённое число: {change_number(second_n, count_numbers(second_n))}")


def count_numbers(n):
	num_count = 0
	while n > 0:
		num_count += 1
		n //= 10
	return num_count


def change_number(n, num_count):
	last_digit = n % 10
	first_digit = n // 10 ** (num_count - 1)
	between_digits = n % 10 ** (num_count - 1) // 10
	n = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
	return n


main()


# Задача 5. Маятник.

def amplitude(start, stop):
	count_num = 0
	while start > stop:
		start -= start * 0.084
		count_num += 1
	return f"Маятник считается остановившимся через {count_num} колебаний"


initial_amplitude = float(input("Введите начальную амплитуду: "))
stop_amplitude = float(input("Введите амплитуду остановки: "))

if initial_amplitude > stop_amplitude:
	print(amplitude(initial_amplitude, stop_amplitude))
else:
	print("Амплитуда остановки не может быть больше начальной амплитуды")

# Задача 6. Яйца.

import scipy.optimize as optimize


def calculate_safe_depth(max_deviation):
	def equation(x):
		return x ** 3 - 3 * x ** 2 - 12 * x + 10

	def optimize_func(x):
		return equation(x) - max_deviation

	safe_depth = optimize.brentq(optimize_func, 0, 4)
	return safe_depth


max_deviation = float(
	input("Введите максимально допустимый уровень опасности: "))

safe_depth = calculate_safe_depth(max_deviation)

print(f"Приблизительная глубина безопасной кладки: {safe_depth} м")

# Задача 6. Яйца. Альтернативное решение
d_from = 0
d_to = 4
max_danger = float(input("Введите максимально допустимый уровень опасности: "))

depth = d_from + (d_to - d_from) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

if max_danger < 0:
	print(
		"Ошибка: максимально допустимый уровень опасности - абсолютная величина и должна быть больше нуля.")
else:
	while abs(danger) > max_danger:
		if danger > 0:
			d_from = depth
		else:
			d_to = depth
		depth = d_from + (d_to - d_from) / 2
		danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
	print(f"Приблизительная глубина безопасной кладки: {depth} м")
