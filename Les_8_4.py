# Задача 1. Прятки

seconds = int(input("Количество секунд: "))
for i in range(seconds, 0, -1):
	print(i)
print("Я иду искать!")

# Задача 2. Армия

soldiers_count = int(input("Введите число солдат: "))
number_bylaws = int(input("Введите число правил в уставе: "))
push_ups = 0
for i in range(soldiers_count - 3, 0, -4):
	soldiers_answer = int(input("Сколько правил в уставе: "))
	if number_bylaws != soldiers_answer:
		print("Неправильно! Упал, отжался:", i * 10, "раз")
		push_ups += i * 10
print("Число отжиманий", push_ups)

# Задача 3. Прятки 2

seconds = int(input("Количество секунд: "))
step = seconds % 2
for i in range(seconds - step, 0, -2):
	print(i)
print("Я иду искать!")
