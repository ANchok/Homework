import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance: int = 0
        self.lock = threading.Lock()

    def deposit(self):
        tran_limit = 100
        while tran_limit:
            dep_sum = randint(50, 500)
            self.balance += dep_sum
            print(f'Пополнение {dep_sum}. Баланс: {self.balance}. Limit: {tran_limit - 1}')

            tran_limit -= 1
            sleep(0.001)

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        tran_limit = 100
        is_out_of_balance = False
        while tran_limit:
            if is_out_of_balance:
                self.lock.acquire()

            take_sum = randint(50, 500)
            print(f'Запрос на {take_sum}')

            if take_sum <= self.balance:
                is_out_of_balance = False
                self.balance -= take_sum
                print(f'Снято: {take_sum}. Баланс: {self.balance}')
            else:
                is_out_of_balance = True
                print(f'Запрос отклонён, недостаточно средств')

            tran_limit -= 1
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
