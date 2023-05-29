# Задача 1. Космическая еда

bag_buckwheat = 100
month = 1
for i in range(bag_buckwheat, -1, -4):
	print("Месяц №", month)
	print("Гречки в запасе:", i)
	print()
	month += 1

# Задача 2. Долги

number_debtors = int(input("Введите количество должников: "))
sum_debt = 0
for i in range(0, number_debtors, 5):
	print("Должник с номером", i)
	dept = int(input("Сколько должны? "))
	sum_debt += dept
print("Общая сумма долга:", sum_debt)

# Задача 3. Микроволновка

reverse_timer = int(input("Введите количество секунд: "))
for i in range(reverse_timer, 0, -1):
	print("Осталось:", i)
	food_ready = int(input(
		"Готовы ли вы забрать еду: Введите '1' - Да, еда готова. Введите '0' - Нет: "))
	if food_ready:
		print("Ваша еда готова, можете забрать")
		break
if not food_ready:
	print("Ваша еда готова, осторожно горячo!")

# Задача 4. Среднее на отрезке

var_a = int(input("Введите число a: "))
var_b = int(input("Введите число b: "))
var_c = int(input("Введите число c: "))
sum_var, count_var = 0, 0
for i in range(var_a, var_b + 1):
	if i % var_c == 0:
		sum_var += i
		count_var += 1
print("Среднее арифметическое", sum_var / count_var)

# Задача 5. Функция-2

var_start = int(input("Введите начало отрезка: "))
var_stop = int(input("Введите конец отрезка: "))
var_step = int(input("Введите шаг: "))

for i in range(var_stop, var_start - 1, var_step):
	res = i ** 3 + 2 * i ** 2 - 4 * i + 1
	print(f"В точке {i} функция равна {res}")

# Задача 6. Стипендия

educational_grant = int(input("Введите стипендию: "))
expenses = int(input("Введите расходы на проживание: "))
monthly_expenses = expenses
not_enough = monthly_expenses - educational_grant
for i in range(1, 11):
	print(
		f"Месяц траты: {round(monthly_expenses, 1)} не хватает {round(not_enough, 2)}")
	if i == 10:
		print(f"Нужно попросить у родителей {round(not_enough, 2)} рублей")
	monthly_expenses *= 1.03
	not_enough = not_enough + monthly_expenses - educational_grant

# Задача 7. Сумма ряда

var_n = int(input("Введите натуральное число N: "))
sum_n = 0
for i in range(0, var_n):
	elem = (-1) ** i * (1 / 2 ** i)
	sum_n += elem
print("Сумма равна:", sum_n)

# Задача 8. Кинотеатр

boys_number = int(input("Введите количество мальчиков: "))
girls_number = int(input("Введите количество девочек: "))
if girls_number == 1 and boys_number == 3 or girls_number == 3 and boys_number == 1:
	print("Ответ: Нет решения")
elif -2 <= boys_number - girls_number <= 2:
	boy, girl, res = 'B', 'G', ''
	if boys_number == girls_number:
		for i in range(boys_number):
			res = res + boy
			res = res + girl
		print(res)
	elif boys_number - girls_number == 1:
		for i in range(boys_number):
			res = res + boy
			res = res + girl
		print(res[:-1])
	elif boys_number - girls_number == 2:
		for i in range(boys_number):
			res = res + boy
			res = res + girl
		print(res[:-5] + res[-4:-1])
	elif girls_number - boys_number == 1:
		for i in range(girls_number):
			res = res + girl
			res = res + boy
		print(res[:-1])
	elif girls_number - boys_number == 2:
		for i in range(girls_number):
			res = res + girl
			res = res + boy
		print(res[:-5] + res[-4:-1])
else:
	print("Ответ: Нет решения")
