def custom_write(file_name: str, string: list) -> dict:
    file = open(file_name, 'r+', encoding='utf-8')
    string_position: dict = {}
    num = 0
    # определяет на какой строке остановилась запись в файле test.txt
    for line in file:
        num += 1
    # запись в словарь
    for item in string:
        string_position[(num + 1, file.tell())] = item
        num += 1
        file.write(item + '\n')
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