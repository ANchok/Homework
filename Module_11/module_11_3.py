import builtins as b
from pprint import pprint


class Example:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def example_method(self):
        print(self.name, self.value)


def introspection_info(obj):
    split_list = str(type(obj)).split("'", 2)
    if '__main__.' in split_list[1]:
        split_list[1] = split_list[1][9:]
    try:
        result = {'type': split_list[1], 'attributes': vars(obj), 'methods': dir(obj), 'module': obj.__module__}
        # убираем атрибуты из списка methods, чтобы не повторяться
        for key in result['attributes'].keys():
            if key in result['methods']:
                result['methods'].pop(result['methods'].index(key))
    except TypeError:
        # случай, когда передаваемый obj не имеет метода __dict__
        try:
            result = {'type': split_list[1], 'methods': dir(obj), 'module': obj.__module__}
        except AttributeError:
            # случай, когда obj не имеет атрибута __module__
            result = result = {'type': split_list[1], 'methods': dir(obj)}
    return result


def pprint_info(obj):
    obj_info = introspection_info(obj)
    pprint(obj_info, sort_dicts=False)


obj = Example('Lime', 23)
pprint_info(obj)
pprint_info(34)
pprint_info(1.2)
pprint_info([1, 2])
pprint_info(pprint)