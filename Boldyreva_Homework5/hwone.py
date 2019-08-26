#ДЗ. Тема 5. Модули и библиотеки
#1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
# Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os, sys

def create_dir():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(),f'dir_{i}')
        os.mkdir(new_path)


def delete_dir():
    for i in range(1,10):
        new_path = os.path.join(os.getcwd(),f'dir_{i}')
        os.rmdir(new_path)
if __name__ == '__main__':
    vopros = int(input('Если вы хотите создать папки введите 1,\nЕсли ходите все удалить введите 2: '))
    if vopros == 1:
        create_dir()
    else:
        delete_dir()