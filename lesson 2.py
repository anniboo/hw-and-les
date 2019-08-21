friends = 'Максим Леонид1'
print(friends)
print(len(friends))
print(friends.find('Лео'))

print(friends.split())

friends = 'Максим;Леонид1'
print(friends.split(';'))

print(friends.isdigit())

number = '123'
print(number.isdigit())

print(friends.upper())
print(friends.lower())

# Форматирование строк
name = 'Leo'
age = 30
#1. конкатенация
hello_str = 'Привет, ' + name + ' тебе ' + str(age) + ' лет'
print (hello_str)
#2.% s - сюда попадает строка, а в "d" попадает число
hello_str = 'Привет %s тебе %d лет'%(name, age)

print (hello_str)
#3(
hello_str = 'Привет {} тебе {} лет'.format(name, age)
print (hello_str)

friend_name = 'Max'
friends = ['Max','Leo','Kate']
roles = ('admin','guest','user')

#while
i = 0
while i < len(friends) :
    friend = friends[i]
    print(friend)
    i+=1

#for
for friend in friends :
