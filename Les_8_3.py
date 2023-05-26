# Задача 1. Степень нечётного числа

var_n = int(input("Введите число: "))
for i in range(1, var_n + 1, 2):
	print(f"{i} ** 2 = {i ** 3}")

# Задача 2. Театр

var_n = int(input("Введите число: "))
sum_chairs = 0
for i in range(1, var_n + 1, 5):
	print("Номер стула:", i)
	sum_chairs += i
print("Сумма:", sum_chairs)

# Задача 3. Диета

awake_time = int(input("Время пробуждения: "))
water, sum_calories = 0, 0
for i in range(awake_time, 23, 3):
	print("На часах:", i)
	water += 1
	calories = int(input("Введите число калорий: "))
	sum_calories += calories
print(f"Вы выпили {water} литров воды и съели {sum_calories} калорий пищи")
