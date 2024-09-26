def calculate_structure_sum(*args):
    structure_list = list(*args)
    if len(structure_list) == 0:
        return 0
    else:
        first = structure_list[0]
        structure_list.pop(0)
        if isinstance(first, int) or isinstance(first, float):
            return first + calculate_structure_sum(structure_list[0:])
        elif isinstance(first, dict):
            value_list = list(first.values())
            key_list = list(first.keys())
            return (calculate_structure_sum(value_list)
                    + calculate_structure_sum(key_list)
                    + calculate_structure_sum(structure_list[0:]))
        elif isinstance(first, tuple):
            tuple_list = list(first)
            if len(tuple_list) == 0:
                return calculate_structure_sum(structure_list[0:])
            else:
                return calculate_structure_sum(tuple_list) + calculate_structure_sum(structure_list[0:])
        elif isinstance(first, str):
            return len(first) + calculate_structure_sum(structure_list[0:])
        else:
            if len(first) <= 1:
                return calculate_structure_sum(first[0])
            else:
                return calculate_structure_sum(first) + calculate_structure_sum(structure_list[0:])


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)