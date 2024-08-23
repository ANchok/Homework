my_dict = {'Gleb': 12041999, 'Anton': 16092001}
print(my_dict)
print(my_dict['Gleb'])
print(my_dict.get('Selin', 'Такого ключа нет'))
my_dict.update({'Lale': 11022003, 'Kate': 10121890})
print(my_dict.pop('Gleb'))
print(my_dict)
my_set = {1, 2, 3.0, 3, 1, 1, 2, 2, True, False, 0, (1, 2, 3), 'Str', 4, 5, 6}
print(my_set)
my_set.add(67)
my_set.add(34)
my_set.remove(3)
print(my_set)
