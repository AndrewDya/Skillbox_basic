# Задача 1. Координаты

x = int(input("Введите x: "))
y = int(input("Введите y: "))
if x > y:
	print(f"{x} > {y}")
if x < y:
	print(f"{x} < {y}")
if x == y:
	print(f"{x} равен {y}")

# Задача 2. Скидки!

bank_total = int(input("Сколько денег на счету? "))
if bank_total >= 75000:
	bank_total -= 75000
	if bank_total < 5000:
		bank_total += 1000
		print("Сделана скидка")
	print("Курс успешно приобретён")
else:
	print("Не хватает денег на счёте")
print("Остаток на счету", bank_total)
print("Хорошего дня!")

# Задача 3

money = int(input("Введите сумму: "))
cheeze_price = 60
ice_cream_price = 20
if money >= cheeze_price:
	money -= cheeze_price
	print("На сыр денег хватило")
	if money >= ice_cream_price:
		print("И на мороженое тоже!")
else:
	print("Денег маловато")
