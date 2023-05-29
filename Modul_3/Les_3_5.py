# Задача 1. Яблоки

veight_apples = 41
full_boxes = 41 // 3
apples_left = 41 % 3
print(f"Ящиков заполнено {full_boxes}, {apples_left} тонны яблок останется")

# Задача 2. Последняя цифра

num = int(input("Введите число: "))
house_num = num % 10
flat_num = num // 10
print(f"Номер дома: {house_num}")
print(f"Номер квартиры: {flat_num}")
