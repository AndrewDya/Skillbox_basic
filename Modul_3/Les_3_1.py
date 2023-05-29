# Задача 1. Пропавшая переменная

client = 'Петя'
pet = 'Кот'
print(client)
print('и')
print(pet)

# Задача 2. Цвета

r = 'Red'
g = 'Green'
b = 'Blue'
# print(r, b, g, r + g + b, b, g + b)
# Red Blue Green RedGreenBlue Blue GreenBlue

# Задача 3. Животные

# «Заяц спит, Черепаха идёт» в одну строку.
first_pet = 'Заяц'
second_pet = 'Черепаха'
print(f"{first_pet} спит, {second_pet} идёт")

# Задача 4. Вход в систему

first_name = input('Введите имя пользователя: ')
greeting = 'Привет'
print(greeting, first_name)
intro, info = "К сожалению, у Вас нет доступа к системе.", "Пожалуйста, обратитесь к системному администратору."
print(intro)
print(info)

# Задача 5. Полёт

city_of_departure = input("Введите город отправления: ")
city_of_arrival = input("Введите город прилёта: ")
print(f"{city_of_departure} - {city_of_arrival}")

# Задача 6. Повышенная сложность. Обмен значений двух переменных

a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
a, b = b, a
print(a, b)
