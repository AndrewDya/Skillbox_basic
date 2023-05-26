# # Задача 1. Должники.
#
# count_number = 0
# for num in range(10):
# 	number = int(input(f"Введите {num + 1} число: "))
# 	if number > 0 and number % 2 == 0:
# 		count_number += 1
# print("Одновременно чётных и положительных чисел: ", count_number)
#
# # Задача 2. Посчитай чужую зарплату...
#
# total_salary = 0
# for count_salary in range(1, 13):
# 	salary = int(input(f"Введите зарплату номер {count_salary}: "))
# 	total_salary += salary
# print(f"Средняя зарплата за год: {round(total_salary / 12, 2)} рублей")
#
# # Задача 3. Факториал.
#
# fact_num = int(input("Введите число: "))
# fact_res = 1
# for i in range(1, fact_num + 1):
# 	fact_res *= i
# print(f"Факториал числа {fact_num} равен {fact_res}")
#
# # Задача 4. Успеваемость в классе.
#
# students_quantity = int(input("Введите количество учеников: "))
# excellent_count, good_count, average_count = 0, 0, 0
# for student in range(students_quantity):
# 	grade = int(input("Введите оценку для ученика (3, 4, 5): "))
# 	if grade == 3:
# 		average_count += 1
# 	elif grade == 4:
# 		good_count += 1
# 	else:
# 		excellent_count += 1
# max_students = excellent_count
# max_category = "Отличники"
# if good_count > max_students:
# 	max_students = good_count
# 	max_category = "Хорошисты"
# if average_count > max_students:
# 	max_students = average_count
# 	max_category = "Троечники"
#
# print(
# 	f"Наибольшее количество студентов: {max_category} в количестве: {max_students} ")
#
# # Задача 5. Отрезок.
#
# num_a = int(input("Введите число a: "))
# num_b = int(input("Введите число b: "))
# quantity, average = 0, 0
# for i in range(num_a, num_b + 1):
# 	if i % 3 == 0:
# 		average += i
# 		quantity += 1
# print(f"Среднее арифметическое: {int(average / quantity)}")
#
# # Задача 6. Замечательные числа.
#
# print("Двузначные числа, равные утроенному произведению своих цифр: ")
# for i in range(10, 100):
# 	if i == 3 * (i % 10) * (i // 10):
# 		print(i)

# Задача 7. Пропавшая карточка.

# Первое решение
cards = int(input("Введите количество карточек: "))
sum_card, sum_all_cards = 0, 0
for i in range(1, cards):
	card = int(input("Введите номер оставшейся карточки: "))
	sum_card += card
	sum_all_cards += i
difference = sum_all_cards + cards - sum_card
print(f"Номер пропавшей карточки: {difference}")

# Второе решение
# list_card = []
# cards = int(input("Введите количество карточек: "))
# for i in range(1, cards):
# 	card = int(input("Введите номер оставшейся карточки: "))
# 	list_card.append(card)
# list_card = sorted(list_card)
# for i in range(1, cards + 1):
# 	if i not in list_card:
# 		print(f"Номер пропавшей карточки: {i}")
