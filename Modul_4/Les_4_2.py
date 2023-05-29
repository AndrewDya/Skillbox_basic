# Задача 1. Сбой

a = 6
b = 2
c = 0
if b < a:
	c = a * b
print(c)

# Задача 2. Курс от Skillbox

bank_total = int(input("Введите состояние своего банковского счёта: "))
if bank_total >= 75000:
	bank_total -= 75000
	print("Покупка совершена успешно")
print("Хорошего дня!")

# Задача 3. Угадай число

son_number = int(input("Введите число от 1 до 10: "))
dad_number = 5
print("Какое число я загадал?", son_number)
if son_number != dad_number:
	print("Не угадал!")
print("Конец игры")
