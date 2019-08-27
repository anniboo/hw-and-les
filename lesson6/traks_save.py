import json

favourite_traks = [
    {'name': 'Вечная Любовь', 'artist': 'Агата Кристи'},
    {'name': ' Angel', 'artist': 'MAssive Attack'},
    {'name': 'Jamming', 'artist': 'Bob Marley'}
]

with open('traks.json','w',encoding='utf-8') as f:
    json.dump(favourite_traks,f)
print('Выполнено')