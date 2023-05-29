# Задача 1. Курс от Skillbox-2

bank_total = int(input("Сколько денег на счету? "))
if bank_total >= 75000:
	bank_total -= 75000
	print("Покупка совершена успешно")
else:
	print("Не хватает денег на счёте")
print("Хорошего дня!")

num_a = int(input("Введите первое число: "))
num_b = int(input("Введите второе число: "))
sum_num = int(input("Сумма этих чисел: "))
if num_b + num_a == sum_num:
	print("Ответ верный")
else:
	print("Ответ неверный")

# Задача 2. Разминка для мозгов

son_number = int(input("Введите число от 1 до 10: "))
dad_number = 5
print("Какое число я загадал?", son_number)
if son_number == dad_number:
	print("Угадал!")
else:
	print("Не угадал")
print("Конец игры")
