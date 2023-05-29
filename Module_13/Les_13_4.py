# Задача 1. Опять налоги


def tax_count(tax, new_tax):
	if tax + new_tax > tax:
		print("Результат: Бюджет увеличится")
	else:
		print("Бюджет не изменится")


tax = float(input("Введите бюджет страны: "))
new_tax = float(input("Новые поступления (налог): "))
tax_count(tax, new_tax)

# def check_budget(old_budget, new_tax):
#     while old_budget % 10 == 0:
#         old_budget /= 10
#         new_tax /= 10
#
#     if int(old_budget + new_tax) == int(old_budget):
#         print("Бюджет не изменился")
#     else:
#         print("Бюджет изменился")
#
# # budget = float(input("Введите бюджет страны: "))
# # new_tax = float(input("Новые поступления (налог): "))
#
# budget = 1.23e2
# new_tax = 1.2e1
# check_budget(budget, new_tax)

# Задача 2. Сравнение

import math


def eqv(num_1, num_2, num_3):
	return math.isclose(num_1 + num_2, num_3)


# def eqv(a, b, c):
#     return abs((a + b) - c) <= 1e-15

print(eqv(1.1, 2.2, 3.3))
