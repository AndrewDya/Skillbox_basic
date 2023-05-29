# Задание 1. Дом для семьи

for meters in 100, 90, 95, 87, 102:
	if meters % 3 == 0:
		print(meters, 'Подходит')
	else:
		print(meters, 'Не подходит')

# Задание 2. Таблица степеней

for num in 3, 7, 5, 6, 4:
	print(f"{num ** 2} {num ** 3} {num ** 4}")

# Задача 3. Лотерея 2

win_count = 0
for num in 345, 19, 87, 1020, 421, 255, 462, 245:
	if 100 <= num < 1000 and num % 5 == 0:
		win_count += 1
		print(f"номер {num} - выигрышный")

print("Число выигрышных билетов:", win_count)
