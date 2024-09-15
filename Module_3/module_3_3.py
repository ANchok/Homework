def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [34, 'str', False]
values_dict = {'a': 4, 'b': 'str', 'c': False}
values_list_2 = [123, True]

# 1
print_params(8, 'not', False)
print_params(34,'key')
print_params(b = 73, c = 'str')
print_params(7)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
# 2
print_params(*values_list)
print_params(**values_dict)
# 3
print_params(*values_list_2, 42)