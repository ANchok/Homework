class StepValueError(ValueError):
    pass


class StopValueError(ValueError):
    def __init__(self, message):
        self.message = message


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start: int = start
        self.stop: int = stop
        self.step: int = step
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')
        if step > 0 and start >= stop:
            raise StopValueError(f'начало >= конец: {self.start} >= {self.stop}'
                                 f' - при положительном шаги: {self.step} > 0')
        elif step < 0 and start <= stop:
            raise StopValueError(f'начало <= конец: {self.start} <= {self.stop}'
                                 f' - при отрицательном шаги: {self.step} < 0')
        self.pointer: int = 0

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration()
            else:
                return self.pointer
        else:
            if self.pointer > self.stop:
                raise StopIteration()
            else:
                return self.pointer


def for_iterator(iter):
    for i in iter:
        print(i, end=' ')
    print()


try:
    iter1 = Iterator(100, 200, 0)
    for_iterator(iter1)
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)

for_iterator(iter2)
for_iterator(iter3)
for_iterator(iter4)

try:
    iter5 = Iterator(10, 1)
    for_iterator(iter5)
except StopValueError as exc:
    print(exc.message)