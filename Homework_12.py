# Задача 1. Сумма чисел.


def amount_n(N):
	sum_n = 0
	for i in range(1, N + 1):
		sum_n += i
	print(f"Я знаю, что сумма чисел от 1 до {N} равна {sum_n}")


var_n = int(input("Введите целое положительное число N: "))
if var_n > 0:
	amount_n(var_n)
else:
	print("Нужно ввести целое положительное число")


# Задача 2. Функция в функции.


def positive():
	print("Положительное")


def negative():
	print("Отрицательное")


def test():
	num = int(input("Введите целое число: "))
	if num > 0:
		positive()
	elif num < 0:
		negative()


test()


# Задача 3. Апгрейд калькулятора.


def max_num(a, b):
	if a > b:
		print(f"Максимальное число: {a}")
	elif a < b:
		print(f"Максимальное число: {b}")
	else:
		print(f"{a}={b}")
	start()


def min_num(a, b):
	if a < b:
		print(f"Минимальное число: {a}")
	elif a > b:
		print(f"Минимальное число: {b}")
	else:
		print(f"{a}={b}")
	start()


def sum_num(a, b):
	print(f"{a}+{b}={a + b}")
	start()


def start():
	var_a = int(input("Введите число a: "))
	var_b = int(input("Введите число b: "))
	choice = int(input(
		"Выберите действие: 1 - вывести сумму цифр, 2 - максимальную цифру, 3 - минимальную цифру: "))
	if choice == 1:
		sum_num(var_a, var_b)
	elif choice == 2:
		max_num(var_a, var_b)
	elif choice == 3:
		min_num(var_a, var_b)
	else:
		print("Ошибка ввода")


start()


# Задача 4. Число наоборот.


def reverse_number(N):
	reverse_n = ''
	while N > 0:
		reverse_n += str(N % 10)
		N //= 10
	if reverse_n[0] == "0" and reverse_n[1] != "0":
		print(f"Число наоборот: {int(reverse_n)}")
	else:
		print(f"Число наоборот: {reverse_n}")


var_n = int(input("Введите число: "))
if var_n != 0:
	reverse_number(var_n)
else:
	print("Программа завершена!")


# Задача 5. Текстовый редактор.

def count_letters(text, search_num, search_letter):
	count_num, count_letter = 0, 0
	for char in text:
		if char == search_num:
			count_num += 1
		elif char.lower() == search_letter.lower():
			count_letter += 1
	print(f"Количество цифр {search_num}: {count_num}")
	print(f"Количество букв {search_letter}: {count_letter}")


text = input("Введите текст: ")
search_num = input("Какую цифру ищем? ")
search_letter = input("Какую букву ищем? ")
count_letters(text, search_num, search_letter)


# Задача 6. НОД.

def greatest_common_divisor(a, b):
	list_a, list_b = [], []
	for i in range(2, a // 2 + 1):
		if a % i == 0:
			list_a.append(i)
			a //= i
		if b % i == 0:
			list_b.append(i)
			b //= i
	common_elements = set(list_a).intersection(set(list_b))
	gcd = 1
	for num in common_elements:
		gcd *= num
	return gcd


var_a = int(input("Введите первое число: "))
var_b = int(input("Введите второе число: "))
print(f"НОД: {greatest_common_divisor(var_a, var_b)}")

# Задача 7. Недоделка.


import random


def rock_paper_scissors():
	player_choice = input("Выберите камень, ножницы или бумагу: ")
	choices = ['камень', 'ножницы', 'бумага']
	computer_choice = random.choice(choices)
	if player_choice == computer_choice:
		print("Ничья")
	elif (
			(player_choice == 'камень' and computer_choice == 'ножницы') or
			(player_choice == 'ножницы' and computer_choice == 'бумага') or
			(player_choice == 'бумага' and computer_choice == 'камень')
	):
		print("Вы выиграли!")
	else:
		print("Вы проиграли.")


def guess_the_number():
	computer_number = random.randint(1, 20)
	player_number = int(input("Выберите число от 1 до 20: "))

	while player_number != computer_number:
		player_number = int(input("Неправильно. Попробуйте еще раз: "))

	print("Вы отгадали!")


def mainMenu():
	while True:
		print("Главное меню")
		print("1. Камень, ножницы, бумага")
		print("2. Угадай число")
		print("3. Выйти")

		choice = input("Выберите игру (1-3): ")

		if choice == "1":
			rock_paper_scissors()
		elif choice == "2":
			guess_the_number()
		elif choice == "3":
			break
		else:
			print("Некорректный выбор. Попробуйте снова.")


mainMenu()
