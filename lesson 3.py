#Делаем игру
#Для начала импортируем встроенный в питон модуль рандом:
import random
#Задаем переменную number, которая генерирует случайное число от 1 до 100
number = random.randint(1, 100)
# Выводим переменную на экран
print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности 1, 2 или 3: '))
max_count = levels[level]

user_count = int(input('Введите кол-во игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}: ')
    users.append(user_name)
print(users)

is_winner = False
winner_name = None
while not is_winner:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_number =int(input('Введите число от 1 до 100: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number :
            print('Ваше число больше загаданного')
        else :
            print('Ваше число меньше загаданного')
else :
    print(f'{winner_name} Поздравляем с Победой!!!')
