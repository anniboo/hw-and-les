#1: Создать модуль music_serialize.py.
#В этом модуле определить словарь для вашей любимой музыкальной группы,
#С помощью модулей json и pickle сериализовать данный словарь в json и в байты,
#вывести результаты в терминал.
#Записать результаты в файлы group.json, group.pickle соответственно.
#В файле group.json указать кодировку utf-8.
#2: Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle,
#прочитать из них информацию.
#И получить объект: словарь из предыдущего задания.

import json, pickle

my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
{'name': 'Шапито','year': 2014}]}

#picle
with open('group.pickle','wb') as f:
    pickle.dump(my_favourite_group,f)


#Json
with open('group.json','w',encoding='utf-8') as f:
    json.dump(my_favourite_group,f)

