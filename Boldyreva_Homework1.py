# Задание 1 введи число
print('Задание 1')
number1 = int(input('Введите число: '))
print(number1 + 2)

#задание 2 число больше 0 и меньше 10
print('Задание 2')
number2 = int(input('Введите число: '))
while number2 <= 0 or number2 >= 10 :
    print('Ваше число должно быть больше 0 и меньше 10.')
    number2 = int(input('Пожалуйста, Введите число: '))

print (number2 ** 2)

#задание 3 Медицинская анкета
print('Задание 3')

last_name = input('Введите свою фамилию: ')
first_name = input('Введите свое имя: ')
age = int(input('Сколько вам полных лет? '))
weight = int(input('Введите ваш вес: '))

if age < 30 and weight >= 50 and weight < 120:
    print(last_name, first_name, age,'год, вес ', weight,' - хорошее состояние')
elif age < 30 and (weight < 50 or weight >= 120):
        print(last_name, first_name, age, 'год, вес ', weight, ' - Вам стоит обратить внимание на свой вес')
elif (weight < 50 or weight >= 120) and age >= 30 and age < 40 :
    print(last_name, first_name, age,'год, вес ', weight,' - следует заняться собой')
elif (weight < 50 or weight >= 120) and age >= 40:
    print(last_name, first_name, age, 'год, вес ', weight, ' - следует обратитьтся к врачу')
#else используется для людей >=30 и >= 40, которые весят от 50 до 120
else :
    print('- Все супер, так держать!')