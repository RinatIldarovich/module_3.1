#1
my_dict = {'Rinat': 1989, 'Masha': 1990, 'Serg': 1991}
print (my_dict)
print (my_dict ['Rinat'])
print (my_dict.get('Rina'))
print (my_dict.get('Gag', 'отсутствует в словаре!'))
my_dict.update({'Anvar': 1989, 'Farit': 1988})
del my_dict ['Rinat']
print (my_dict)
a=my_dict.pop ('Farit')
print (a)
print(my_dict)

#2
my_set = {23,444,11,'aca',1, 0.1,23,444,11,21}
print(my_set)
my_set.add(66) # как добавить 2 элемента?
my_set.add(77)
print(my_set)
my_set.remove(444)
print(my_set)