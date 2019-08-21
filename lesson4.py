def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(number):
    return number % 2 == 0
print(my_filter(numbers,is_even))
#или через лямбда
print(my_filter(numbers, lambda number: number %2 ==0))

def not_even(number):
    return number % 2 != 0

print(my_filter(numbers,not_even))

def big_for(number):
    return number > 4

print(my_filter(numbers,big_for))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(sorted(numbers))
print(sorted(numbers, reverse= True))
#А если нам нужна сортировка по параметрам????

cities = [('Москва', 1000),('Лас-Вегас', 500),('Антверпен', 2000)]

print(sorted(cities))
#А если по численности населения?

def by_count(city):
    return city[1]
print(sorted(cities, key = by_count))

print(sorted(cities, key= lambda city: city[1]))

result = filter(is_even,numbers)
print(list(result))

names = ['max','leo','kate']
print(list(filter(lambda x: len(x)>3, names)))

print(list(map(lambda y: y**2,numbers)))

print(list(map(lambda y: str(y),numbers)))