import threading
from time import sleep, time


class Knight(threading.Thread):
    ENEMY_COUNT = 100

    def __init__(self, name:str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def fight(self, enemy_count=ENEMY_COUNT):
        day_count = 0
        while enemy_count:
            enemy_count -= self.power
            day_count += 1
            sleep(1)
            print(f'{self.name} сражается {day_count} день(дня)..., осталось {enemy_count} воинов.')
        print(f'{self.name} одержал победу спустя {day_count} дней(дня)!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
Knight.join(first_knight)
print('Все битвы закончились!')