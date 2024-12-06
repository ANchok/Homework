from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words: tuple = words

    def __call__(self):
        return choice(self.words)


def get_advanced_writer(file_name: str):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for line in data_set:
                file.write(f'{line}\n')

    return write_everything


first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

write = get_advanced_writer('text_9_4.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())