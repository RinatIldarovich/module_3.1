# 'module_1_5.py'
immutable_var = 35, 1989, 'Rinat', 4.5, True
print (immutable_var)
# immutable_var [0]=34
# TypeError: 'tuple' object does not support item assignment
# Ошибка буквально сообщает нам, что кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 3, 4, 6, 7]
print (mutable_list)
mutable_list [0]= 10, 20
print (mutable_list)