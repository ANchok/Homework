class Horse:
    def __init__(self, x_distance=0, y_distance=0, sound='Frr'):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__(y_distance)

    def run(self, dx):
        self.x_distance += int(dx)


class Eagle:
    def __init__(self, x_distance=0, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += int(dy)


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance=0, y_distance=0, sound='Frr'):
        super().__init__(x_distance, y_distance, sound)


    def move(self, dx, dy):
        super().run(int(dx))
        super().fly(int(dy))

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()