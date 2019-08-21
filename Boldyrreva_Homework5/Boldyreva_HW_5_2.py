#2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный
# элемент. Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
# Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random
listik = [1, 2, 3, 4]
listok = []
def spisok(list):
    if len(list) == 0:
        return None
    else:
        result = random.choice(list)
        return result

h = spisok(listik)
print(h)
m = spisok(listok)
print(m)