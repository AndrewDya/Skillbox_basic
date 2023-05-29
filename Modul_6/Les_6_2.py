# Задача 1. Циклы — это сложно?

number = int(input("Введите число: "))
sum = 0
while number != 0:
	sum += number
	number = int(input("Введите число: "))
print(sum)

# Задача 2. Введите пароль

password = int(input("Введите пароль: "))
while password != 235:
	print("Неверный пароль!")
	password = int(input("Попробуйте ещё раз:"))
print("Пароль верный! Добро пожаловать.")

# Задача 3. Накопления

cash = 0
while cash < 500000:
	cash += int(input("Сколько отложить денег? "))
print("Сумма накопилась")
