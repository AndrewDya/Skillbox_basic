# Задача 1. Надоедливый заказчик

count_text = int(input(("Введите количество выводов: ")))
count = 0
while count_text != count:
	print("Я - программист!")
	count += 1

# Задача 2. Напоминалка

count_message = int(input("Введите количество раз для напоминания: "))
while count_message != 0:
	print("Вы хотели не забыть о чём-то")
	count_message -= 1

# Задача 3. Рыбалка

n = int(input("Сколько раз ходили перетаскивать? "))
total_weight = 0
while n != 0:
	bags_weight = int(input("Введите вес очередного мешка: "))
	total_weight += bags_weight
	n -= 1
print("Суммарный вес:", total_weight)
