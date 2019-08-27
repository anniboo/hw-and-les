import json

friends = [{'name':'Max','age': 23, 'phones':[123,234]},
           {'name':'Leo','age': 33}
]
#посмотрим тип объекта
print(type(friends))

#преобразуем список друзей в json
json_friends = json.dumps(friends)

#ппечватаем что вышло
print(json_friends)
#проверим тип
print(type(json_friends))

friends = json.loads(json_friends)
print(friends)
print(type(friends))