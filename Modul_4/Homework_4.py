# # Задача 1.
rain = int(input("Идёт ли на улице дождь? 1 - да, 0 - нет: "))
if rain:
	print("Пошёл дождь. Возьмите зонтик!")
else:
	print("Дождя нет!")

# # Задача 2.
russian = int(input("Введите количество баллов по русскому языку: "))
math = int(input("Введите количество баллов по математике: "))
computer_science = int(input("Введите количество баллов по информатике: "))
if russian + math + computer_science >= 270:
	print("Поздравляю, ты поступил на бюджет!")
else:
	print("К сожалению, ты не прошёл на бюджет.")

# # Задача 3
day = int(input("Введите день: "))
if day % 2 == 0:
	print("Сегодня рабочий день")
else:
	print("Сегодня выходной!")

# Задача 4
first_chair = int(input("Введите цену первого стула: "))
second_chair = int(input("Введите цену второго стула: "))
third_chair = int(input("Введите цену третьего стула: "))
total = first_chair + second_chair + third_chair
if total > 10000:
	total = total - (total / 10)
	print("Сумма чека:", total)
else:
	print("Сумма чека:", total)

# # Задача 5
x = int(input("Введите число x: "))
if x >= 0:
	print("Ответ:", x)
else:
	x = -x
	print("Ответ:", x)

# Задача 6
cube_player = int(input("Кубик игрока: "))
cube_owner = int(input("Кубик владельца: "))
if cube_player >= cube_owner:
	print("Разность:", cube_player - cube_owner)
	print("Игрок платит")
else:
	print("Сумма:", cube_player + cube_owner)
	print("Владелец платит")
print("Игра окончена")

# # Задача 7
hours = int(input("Количество отработанных часов: "))
loan_balance = int(input("Остаток по кредиту: "))
spending_on_food = int(input("Количество денег на еду: "))
salary = (200 * hours) / (2 ** 3) + hours
if salary > spending_on_food + loan_balance:
	print("Часов хватает. Можно отдохнуть")
else:
	print("Часов не хватает. Придётся работать больше!")

# Задача 8
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
if a >= b:
	max_num = a
else:
	max_num = b
if max_num > c:
	print("Максимальное число", max_num)
else:
	print("Максимальное число", c)

# max_num = a if a >= b else b
# print("Максимальное число:", max_num if max_num > c else c)
