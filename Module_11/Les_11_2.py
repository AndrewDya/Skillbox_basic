# Задача 1. Ставки на спорт

bid = int(input("Сколько ставим? "))
coefficient = float(input("Какой коэффициент? "))
print(f"Потенциальный выигрыш: {round(bid * coefficient, 2)}")

# Задача 2. День рождения

age = int(input("Введите возраст: "))
temperature = float(input("Введите температуру: "))
print(f"Подарок на день рождения: {round(age * 1.5 * temperature, 0)} рублей")

# Задача 3. Индекс массы тела

weight = float(input("Введите вес (в кг): "))
height = float(input("Введите рост (в м): "))
bmi = round(weight / height ** 2, 2)
if bmi < 18.5:
	print("Индекс массы ниже нормы")
elif bmi < 25:
	print("Индекс массы тела в норме")
elif bmi < 30:
	print("Индекс массы тела выше норме (избыток)")
else:
	print("Индекс массы тела выше норме (ожирение)")
