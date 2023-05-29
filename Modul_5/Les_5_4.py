# Задача 1. Покупка велосипеда

bike_year = int(input("Введите год выпуска: "))
speed_number = int(input("Введите количество скоростей: "))
if bike_year < 2018 and speed_number > 24:
	print("Подходит")
else:
	print("Велосипед не подходит")

# Задача 2. Как поступить?

exam_res = int(input("Сколько баллов набрал? "))
medal = int(
	input("Есть ли золотая медаль (0 — нет медали, 1 — медаль есть): "))
if exam_res > 280 and medal == 1:
	print("Поздравляем! Ты поступил!")
else:
	print("К сожалению, ты не прошёл в наш университет")

# Задача 3. Бактерии живут комфортно

temperature = int(input("Введите значение температуры: "))
if 0 > temperature or temperature > 100:
	print("Danger zone of temperature")
