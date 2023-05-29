# Задача 1. Космические рейнджеры

chatly = int(input("Колько чатлов? "))
loans = chatly / 2200
print(f"Это {loans} CR")
print("Можно купить кораблей:", int(loans / 0.5))

# Задача 2. Компьютерное зрение

coordinate_x, coordinate_y = 0, 0


class NewEx(Exception):
	pass


try:
	print("Введите расположение фигуры")
	coordinate_x = float(input("По горизонтали: "))
	coordinate_y = float(input("По вертикали: "))
	if coordinate_x > 0.8 or coordinate_y > 0.8 or coordinate_x < 0 or coordinate_y < 0:
		raise NewEx
	coordinate_x = int(coordinate_x * 10)
	coordinate_y = int(coordinate_y * 10)
	print(f"Фигура находится в клетке ({coordinate_x}, {coordinate_y})")
except NewEx:
	print("Клетки с такой координатой не существует")


# Задача 3. Точность и аккуратность

class NewEx(Exception):
	pass


try:
	print("Введите расположение фигуры")
	coordinate_x = float(input("По горизонтали: "))
	coordinate_y = float(input("По вертикали: "))
	if coordinate_x > 0.8 or coordinate_y > 0.8 or coordinate_x < 0 or coordinate_y < 0:
		raise NewEx
	coordinate_x_correct = round(
		round(coordinate_x / 0.05) * 0.05 - coordinate_x, 3)
	coordinate_y_correct = round(
		round(coordinate_y / 0.05) * 0.05 - coordinate_y, 3)
	print(
		f"Фигура находится в клетке ({int(coordinate_x * 10)}, {int(coordinate_y * 10)})")
	print(
		f"Поправьте положение фигуры на ({coordinate_x_correct}, {coordinate_y_correct})")
except NewEx:
	print("Клетки с такой координатой не существует")
