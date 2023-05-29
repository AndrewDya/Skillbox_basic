# Задача 1. Неправильный таймер

count = 10
while count >= 0:
	if count == 0:
		print('Время вышло!')
	else:
		print(count)
	count -= 1

# Задача 2. Тестируем приложение

message = 1
while message:
	message = int(input("Продолжаем работать? 1/0: "))
	if message == 0:
		print("Приложение закрывается…")
print("Работа завершена")

# Задача 3. Вирус

code = "0"
while code != "0550":
	print("Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!")
	code = input("Введите код: ")
print("Код верный, завершаю работу...")
