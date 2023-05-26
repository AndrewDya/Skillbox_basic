# Задача 1. Урок литературы

students = 5
count_bad_students = 0
answer = 'пушкин'
for i in range(students):
	answer_student = input("Кто написал произведение? ")
	if answer == answer_student.lower():
		print("Продолжим урок")
		break
	count_bad_students += 1
print("Число 'плохих' студентов", count_bad_students)

# Задача 2. Начальник

right_answer = 'да, конечно, сделал'
answer = ''
while right_answer != answer.lower():
	answer = input("Выполнил ли задание, которое выдавали вчера: ")

# Задача 3. Дразнилка

name = input("Как Вас зовут? ")
print(f"{name}, купи слона")
while True:
	answer = input("")
	print(f"Все говорят {answer}, а ты купи слона!")
