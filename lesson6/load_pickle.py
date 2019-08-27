import pickle

person = {'name':'Max','phones':[123,345]}

#открываем файл
with open('person.dat','rb') as f:
    #сразу читаем объект из файла который мы открыли с помощью pickle
    person = pickle.load(f)

print(person)