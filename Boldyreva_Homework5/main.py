#3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
#Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.

import hwone
from hwtwo import spisok
#Удаление и создание папок из задания 1
pu = input('Создать папку: 1, удалить папки: 2 \n(чтобы пропустить задание набери что угодно): ')
if pu == '1':
    hwone.create_dir()
elif pu == '2':
    hwone.delete_dir()
else:
    print("идем дальше")

#Пробуем с hwtwo со списком
input('нажми Enter, чтобы проверить работает ли мое второе задание')
sp = [1, 2, 33, 21, 23, 22, 11, 5, 90]

print(spisok(sp))