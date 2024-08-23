immutable_var = (1, 'String', True, [1, 2], 1.5)
print(immutable_var)
# immutable_var[0] = 2 # я не могу изменить объект (свойство кортежа) + число 1 не изменяемый тип
immutable_var[3][0] = 4 # я не могу изменить объект (список) на другой, но могу изменить содержимое списка (изменяемый тип)
print(immutable_var)
mutable_list = [1, 3.0, 'TXT', False]
mutable_list[0] = 42
mutable_list[1] = mutable_list[1] + 1
mutable_list[2] = 'Str'
mutable_list[3] = True
print(mutable_list)