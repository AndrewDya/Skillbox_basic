# Задача 1. Робот

def greeting():
    print('Привет!')
    print('Добро пожаловать!')


while True:
    var_a = input('Зайдёте? Да/Нет: ')
    if var_a == 'Да':
        greeting()
    print('Следующий.\n')


# Задача 2. Провизия

def count_a_b():
    a = int(input())
    b = int(input())
    print("Всего", a + b, "шт.")


print("Сколько мешков рыбы и мяса?")
count_a_b()

print("Сколько буханок белого и чёрного хлеба?")
count_a_b()

print("Сколько вёдер воды и молока?")
count_a_b()


# Задача 3. Почта


def info():
    print("Фамилия: Иванов")
    print("Имя: Василий")
    print("Улица: Пушкина")
    print("Дом: 32")
    print()


info()
info()
info()
