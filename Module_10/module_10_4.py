import threading
from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number: str, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name: str):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables: tuple = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        is_all_taken = False
        # рассаживаем гостей, пока есть свободные столы
        for guest in guests:
            is_sat_down = False
            # ищем свободный стол
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    is_sat_down = True
                    table.guest.start()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    break
            # проверяем сел гость в этой итерации за стол или нет
            # если нет, значит все столы заняты
            if not is_sat_down:
                is_all_taken = True
                break

        # если появился гость, которому нет места, тогда его и остальных в очередь
        if is_all_taken:
            for i in range(len(self.tables), len(guests)):
                guest = guests[i]
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or not self.is_all_free_tables():
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest.start()

    def is_all_free_tables(self) -> bool:
        result = True
        for table in self.tables:
            if table.guest is not None:
                result = False
                break
        return result


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
