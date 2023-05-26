temperature = int(input("Введите температуру: "))
distance = 0
while temperature >= 15:
	distance += 20
	temperature -= 2
	if temperature <= 15:
		break
	distance += 10
print("Шагов пройдено", distance)

number = int(input("Введите число: "))
total = 0
while number > 0:
	last_number = number % 10
	total += last_number
	if last_number == 5:
		print("Обнаружен разрыв")
		break
	number //= 10
print("Сумма цифр", total)

money = int(input("Введите начальное количество денег: "))
while money < 10000:
	cube = int(input("Введите число, которое выпало на кубике: "))
	if cube == 3:
		money = 0
		print("Вы проиграли всё")
		break
	money += 500
print("Игра закончена")
print("Итого осталось", money)
