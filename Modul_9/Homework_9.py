# Задание 1. «Я стал новым пиратом!»

key_word = 'карамба'
sum_words = 0
for i in range(10):
	word = input("Введите ключевое слово: ")
	if key_word == word.lower():
		sum_words += 1
print("На борт попало:", sum_words, "человек")

# Задание 2. Кривой мессенджер

message = input('Введите текст: ')
symbol_count = 0
for symbol in message:
	symbol_count += 1
	if symbol == '*':
		print("Символ «*» стоит на позиции", symbol_count)
		break

# Задание 3. Театр

row_number = int(input("Введите кол-во рядов: "))
seats_in_row = int(input("Введите кол-во сидений в ряде: "))
distance_between_rows = int(input("Введите кол-во метров между рядами: "))
print("Сцена")
for i in range(row_number):
	print("=" * seats_in_row, end=' ')
	print("*" * distance_between_rows, end=' ')
	print("=" * seats_in_row)

# Задание 4. Марсоход-2

coordinate_x = 8
coordinate_y = 10
while True:
	print(
		f"[Программа]: Марсоход находится на позиции {coordinate_x}, {coordinate_y}, введите команду:")
	operator = input("[Оператор]: ").upper()
	if operator == 'W' and coordinate_y != 20:
		coordinate_y += 1
	elif operator == 'S' and coordinate_y != 0:
		coordinate_y -= 1
	elif operator == 'D' and coordinate_x != 15:
		coordinate_x += 1
	elif operator == 'A' and coordinate_x != 0:
		coordinate_x -= 1
	elif operator == 'stop':
		break

# Задание 5. Великий и могучий

text = input("Введите текст: ")
words = text.split()
max_length = 0
for word in words:
	if len(word) > max_length:
		max_length = len(word)
print(f"Самое длинное слово, {max_length} букв")

# Задание 6. Коровы

place_cow = input("Введите 10 символов 'a' (свободно) или 'b' (занятое): ")
liters = 0
milk = 0
for symbol in place_cow:
	liters += 2
	if liters == 22:
		break
	if symbol.lower() == 'b':
		milk += liters
print("Молока за день:", milk)

# Задание 7. Метод бутерброда

word = input("Введите зашифрованное сообщение: ")
new_word = ''
if len(word) % 2 == 0:
	for symbol in word[::2]:
		new_word += symbol
	for symbol in word[::-2]:
		new_word += symbol
else:
	start = len(word) - 2
	for symbol in word[::2]:
		new_word += symbol
	for symbol in word[start::-2]:
		new_word += symbol
print("Расшифрованное сообщение:", new_word)

# word = 'seahncdiw' new_word = 'sandwiche'
# word = 'shacnidw' new_word = 'sandwich'
