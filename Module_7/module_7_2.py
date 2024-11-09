def custom_write(file_name: str, string: list) -> dict:
    file = open(file_name, 'w', encoding='utf-8')
    string_position = {}
    i = 0
    for item in string:
        string_position[(i, file.tell())] = item
        i += 1
        file.write(item + '\n')
    print(file.tell())
    file.close()
    return string_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)