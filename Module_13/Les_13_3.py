# Задача 1. Возможности компьютера


num, count_num = 1, 0
while num != 0:
	num /= 2
	count_num += 1
print("Счётчик операций:", count_num)

# Задача 2. Тестирование

var_n = float(input("Введите число в экспоненциальной форме: "))
var_x = 1
sum_count = 1
while var_x + var_n < 2:
	var_x += var_n
	sum_count += 1
print(sum_count)

# Задача 3. Урок информатики

var_x = int(input("Введите число: "))
temp = var_x
degree = 0
while temp > 9:
	temp //= 10
	degree += 1
var_x /= 10 ** (degree)
print(f"Формат плавающей точки: x = {var_x} * 10 ** {degree}")
