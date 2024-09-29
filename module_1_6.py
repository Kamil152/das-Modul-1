#Работа со словарями
my_dict = {'Jesus': 1570,'Moses': 0,'Muhammad': 2140}
print(my_dict)
print(my_dict.get('Jesus'))
print(my_dict.get('Buddha'))
my_dict.update({'David': 530,
                'Vova': 3522})
a=my_dict.pop('Vova')
print(a,'-Удаленное значение из словаря')
print(my_dict)
#Работа со множествами
my_set= {1,1,2,2,3,4,4,4,5,5,5,'duck',True}
print(my_set)
my_set.add(7)
my_set.discard(4)
print(my_set)