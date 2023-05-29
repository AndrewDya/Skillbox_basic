# Задача 1. Калькулятор опыта

experience_points = int(input("Введите число очков опыта: "))
level = 1
if experience_points < 1000:
	print("Уровень героя", level)
elif experience_points < 2500:
	level += 1
	print("Уровень героя", level)
elif experience_points < 5000:
	level += 2
	print("Уровень героя", level)
else:
	level += 3
	print("Уровень героя", level)

# Задача 2. Функция

x = int(input("Введите значение x: "))
y = 0
if x > 0:
	y = x - 12
elif x < 0:
	y = x * x
else:
	y = 5
print("Игрек равен", y)

# Задача 3. Поступление

student_number = int(input("Введите место в списке поступающих: "))
student_scores = int(input("Введите количество баллов за экзамены: "))
if 0 < student_number < 11:
	print("Поздравляем, вы поступили!")
	if student_scores > 290:
		print("Бонусом вам будет начисляться стипендия.")
	else:
		print("Но вам не хватило баллов для стипендии")
else:
	print("К сожалению, вы не поступили.")

# Задача 4. Опять двойка

rating = int(input('Что получил по математике? '))
if rating == 2 or rating == 3:
	print('Плохо. Марш учиться!')
elif rating == 4 or rating == 5:
	print('Молодец! Можешь отдохнуть.')

# Задача 5. Вася хочет выигрывать

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a == b and b == c:
	print(3)
elif a == b or b == c or a == c:
	print(2)
else:
	print(1)

# Задача 6. Новоселье

square_flat = int(input("Введите площадь квартиры (м^2): "))
price_flat = int(input("Введите цену квартиры (млн): "))

if square_flat > 100 and price_flat < 10 or square_flat > 80 and price_flat < 7:
	print("Квартира подходит")

# Задача 7. Почта

hours = int(input("Введите время в часах: "))
if 8 <= hours < 10 or 18 <= hours < 22:
	print("Можно получить посылку")
else:
	print("Посылку получить нельзя")
