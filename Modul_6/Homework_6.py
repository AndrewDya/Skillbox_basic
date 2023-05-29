# # Задача 1. Кубы чисел

num_n = int(input("Введите число, до которого будем возводить в степень 3: "))
count_n = 1
while count_n <= num_n:
	print(f"{count_n}^3={count_n ** 3}")
	count_n += 1

# # Задача 2. Коллекторы

debtor_name = input("Введите имя должника: ")
debt_amount = int(input("Введите сумму долга: "))
total_amount = 0
print(f"{debtor_name}, ваша задолженность составляет {debt_amount} рублей")
while total_amount < debt_amount:
	cash = int(
		input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
	total_amount += cash
	if total_amount >= debt_amount:
		print("Отлично, Василий! Вы погасили долг. Спасибо!")
		break
	else:
		print("Маловато, Василий. Давайте ещё раз.")

# Задача 3. Слишком большие числа

number = int(input("Введите число для расчета: "))
total_count = 1 if number == 0 else 0
while number != 0:
	number = number // 10
	total_count += 1
print("Количество цифр в числе:", total_count)

# Задача 4. Поставьте оценку!

reviews_count_positive, reviews_count_negative, grade = 0, 0, 1
while grade != 0:
	grade = int(input("Введите оценку от −100 до 100: "))
	if grade > 0:
		reviews_count_positive += 1
	elif grade < 0:
		reviews_count_negative -= 1
print("Кол-во положительных отзывов:", reviews_count_positive)
print("Кол-во отрицательных отзывов:", reviews_count_negative)

# Задача 5. Обычный день на работе

print("Начался восьмичасовой рабочий день")
count_hours, count_tasks, store_flag = 1, 0, False
while count_hours <= 8:
	print(f"{count_hours}-ый час")
	tasks = int(input("Сколько задач решит Максим? "))
	count_tasks += tasks
	wife_call = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
	if wife_call == 1:
		store_flag = True
	count_hours += 1
print(f"Рабочий день закончился. Всего выполнено задач: {count_tasks}")
print("Нужно зайти в магазин.") if store_flag else None

# Задача 6. Вклады

contribution_x = int(input("Введите сумму вклада: "))
interest_p = int(input("Введите %: "))
amount_y = int(input("Введите конечную сумму: "))
years_count = 0
while contribution_x < amount_y:
	contribution_x = contribution_x + int(contribution_x * (interest_p / 100))
	years_count += 1
print(f"Спустя {years_count} лет, вы получите {amount_y}")

# Задача 7. Игра «Угадай число»

number = int(input("Введите число от 1 до 10: "))
hidden_number, attempt_counts = 7, 1
while hidden_number != number:
	if number > hidden_number:
		print("Число больше, чем нужно. Попробуйте ещё раз!")
	else:
		print("Число меньше, чем нужно. Попробуйте ещё раз!")
	attempt_counts += 1
	number = int(input("Введите число: "))
print("Вы угадали! Число попыток:", attempt_counts)

# Задача 8. Игра «Компьютер угадывает число»

boy_number = int(input("Загадайте число от 1 до 100: "))
computer_number, answer_boy, count_number = 50, 0, 1
COUNT = 50
print(f"{count_number} попытка, число: {computer_number}")
while computer_number != boy_number:
	if boy_number > computer_number:
		answer_boy = 2
	elif boy_number < computer_number:
		answer_boy = 3
	if answer_boy == 2:
		computer_number = computer_number + COUNT // 2
		if COUNT > 1:
			COUNT //= 2
		elif COUNT == 1:
			computer_number = computer_number + COUNT
	elif answer_boy == 3:
		computer_number = computer_number - COUNT // 2
		if COUNT > 1:
			COUNT //= 2
		elif COUNT == 1:
			computer_number = computer_number - COUNT
	count_number += 1
	print(f"{count_number} попытка, число: {computer_number}")
print(
	f"{computer_number} = {boy_number}, за {count_number} попыток")
