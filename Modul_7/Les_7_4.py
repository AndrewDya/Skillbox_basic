# Задача 1. Квадраты превратились в кубы

for i in range(11):
	print(i ** 3)

# Задача 2. Сумма чисел

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
sum_num = 0
for i in range(first_num, second_num + 1):
	sum_num += i
print(f"Сумма чисел от 5 до 10 равна {sum_num}")

# Задача 3. Поел — можно и поспать, поспал — можно и поесть

awake_time = int(input("Введите час пробуждения: "))
calories, time_wakefulness = 0, 0
for hour in range(awake_time, 23):
	print("Сейчас", hour, "часов")
	eat_calories = int(input("Сколько съели сейчас? "))
	calories += eat_calories
	if calories > 2000:
		print("Пора спать")
		break
	time_wakefulness += 1
print("Съедено калорий", calories)
print("Часов бодрствования", time_wakefulness)
