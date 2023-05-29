# Задача 1. Python!
text = 'Python!'
for symbol in text:
	print(symbol)

# Задача 2. Вирус
text = input("Введите текст: ")
for symbol in text:
	print(symbol * 3)

# Задача 3.
text = input("Введите текст: ")
count_big, count_small = 0, 0

for symbol in text:
	if symbol == 'Ы':
		count_big += 1
	if symbol == 'ы':
		count_small += 1

print("Больших букв Ы:", count_big)
print("Маленьких букв Ы:", count_small)
