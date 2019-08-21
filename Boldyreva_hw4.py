#Тема 4. Функции.
#1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в
print(' Задание 1 \n')
name = input('Введите свое имя: ', )
age = input('Введите свой возраст: ')
city = input('Введите город проживания: ')
def profile(name,age,city):
    stroka = f'{name}, {age} год(а), проживает в городе {city}'
    return stroka
result = profile(name,age,city)
print(result)

#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
print('\n Задание 2 \n')
first = int(input('Введите первое число: ', ))
second = int(input('Введите второе число: ', ))
fhird = int(input('Введите третье число: ', ))

def number(first,second,fhird):
    list =[first,second,fhird]
    second_result = max(list)
    return second_result
max_value = number(first,second,fhird)
print(f'Максимальное число {max_value}')

#3: Давайте опишем пару сущностей player и enemy через словарь
print('\n Задание 3 \n')
import random

player_name = input('Введите свое имя: ')
player = {'name': player_name,'health': 100, 'damage': 50}
enemy = {'name': 'Boss_One','health': 100, 'damage': 50}


def lets_play(player,enemy):
    while player['health'] >0 and enemy['health'] >0:
        player1 = random.randint(1,2)
        if player1 == 2:
            player['health'] = player['health']-enemy['damage']
            if player['health'] <= 0:
                print ("Вам нанесли сокрушительный удар и Вы проиграли")
            else:
                print(f"{enemy['name']} нанес {player['name']} удар. У {player['name']} осталось {player['health']} здоровья")
        else:
            enemy['health'] = enemy['health']-player['damage']
            if enemy['health'] <= 0:
                print("Вы нанесли решающий удар и выиграли")
            else:
                print(f"{player['name']} нанес удар, у {enemy['name']} осталось {enemy['health']} здоровья")
lets_play(player,enemy)

print('\n Задание 4 (с броней)\n')
#4: Давайте усложним предыдущее задание.
player_name = input('Введите свое имя: ')
player = {'name': player_name,'health': 100, 'damage': 40,'armor': 1.2}
enemy = {'name': 'Boss_One','health': 100, 'damage':40,'armor': 1.2}

def damage_calc(damage,armor):
    damage = damage / armor
    return damage

def lets_playtogever(player,enemy):
    new_player_damage = damage_calc(player['damage'],enemy['armor'])
    new_enemy_damage = damage_calc(enemy['damage'],player['armor'])
    while player['health'] >0 and enemy['health'] >0:
        player1 = random.randint(1,2)
        if player1 == 2:
            player['health'] = round(player['health']-new_enemy_damage,2)
            if player['health'] <= 0:
                print ("Вам нанесли сокрушительный удар и Вы проиграли")
            else:
                print(f"{enemy['name']} нанес {player['name']} удар. У {player['name']} осталось {player['health']} здоровья")
        else:
            enemy['health'] = round(enemy['health'] - new_player_damage,2)
            if enemy['health'] <= 0:
                print("Вы нанесли решающий удар и выиграли")
            else:
                print(f"{player['name']} нанес удар, у {enemy['name']} осталось {enemy['health']} здоровья")

lets_playtogever(player,enemy)
