# Задача 1. Среднее арифметическое


import math


def average():
    print((var_a + var_b) / 2)


var_a = int(input("Введите число a: "))
var_b = int(input("Введите число b: "))
if var_a < var_b:
    average()
else:
    print("Неверный диапазон")


# Задача 2. Почта 2

def info(last_name, first_name, residence_country, city, street, house_number,
         apartment_number):
    print("Фамилия:", last_name)
    print("Имя:", first_name)
    print("Страна проживания:", residence_country)
    print("Город:", city)
    print("Улица:", street)
    print("Номер дома:", house_number)
    print("Номер квартиры:", apartment_number)


info("Гридчина", "Анастасия", "Германия", "Берлин", "Wall Street", "25", "56")
print()
info("Петрович", "Юрий", "США", "Бруклин", "Wall Street", "40", "72")
print()
info("Хомка", "Александр", "Америка", "Квинс", "Wall Street", "50", "60")

# Задача 3. GPS-навигатор 2.0


def distance(x, y):
    distance = round(math.sqrt(x ** 2 + y ** 2), 2)
    print(f"Расстояние между двумя точками: {distance}")


def between_distance(x1, y1, x2, y2):
    distance = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
    print(f"Расстояние между двумя точками: {distance}")


choice = int(input(
    "Найти расстояние от себя до точки (0) или найти расстояние между двумя произвольными точками (1): "))
if choice == 0:
    var_x = int(input("Введите координату x: "))
    var_y = int(input("Введите координату y: "))
    distance(var_x, var_y)
elif choice == 1:
    var_x1 = int(input("Введите первую координату x: "))
    var_y1 = int(input("Введите первую координату y: "))
    var_x2 = int(input("Введите вторую координату x: "))
    var_y2 = int(input("Введите вторую координату y: "))
    between_distance(var_x1, var_y1, var_x2, var_y2)
else:
    print("Введены неправильные значения")
