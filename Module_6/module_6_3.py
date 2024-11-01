class Horse:
    def __init__(self, x_distance=0, sound='Frr'):
        self.x_distance: int = x_distance
        self.sound: str = sound

    def run(self, dx: int):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance: int = y_distance
        self.sound: str = sound

    def fly(self, dy: int):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx: int, dy: int):
        self.run(dx)
        self.fly(dy)

    def get_pos(self) -> tuple:
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()