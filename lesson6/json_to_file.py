import json

friends = [{'name':'Max','age': 23, 'phones':[123,234]},
           {'name':'Leo','age': 33}
]
#посмотрим тип объекта
print(type(friends))

with open('friends.jon','w') as f:
    #преобразуем список друзей в json
    json_friends = json.dump(friends, f)

#обратно из файла  в объект
with open('friends.jon','r') as f:
    friends = json.load(f)
print(friends)
print(type(friends))