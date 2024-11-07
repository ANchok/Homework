from math import sqrt


class Figure:
    sides_count: int = 0
    is_equilateral: bool = False    # равносторонность фигуры

    def __init__(self, color: tuple, *sides, filled=True):
        if self.__is_equilateral():                          # проверка на равносторонность
            if len(sides) == 1:                              # сколько длин сторон передано: один или больше
                self.__sides = self.eq_sides(*sides)
            else:
                if self.__is_valid_sides(*sides):
                    if self.is_eq(*sides):
                        self.__sides = list(sides)
                    else:
                        self.__sides = self.eq_sides(1)
                else:
                    self.__sides = self.eq_sides(1)
        else:
            if self.__is_valid_sides(*sides):
                self.__sides = list(sides)
            else:
                self.__sides = self.eq_sides(1)
        self.__color: list = list(color)
        self.filled: bool = filled

    # метод возвращающий список из элемента sides с кол-вом равным sides_count
    # т.е. список из одинаковых элементов
    def eq_sides(self, *sides) -> list:
        return list(sides) * self.sides_count

    # проверяет переданный набор элементов на равенство
    def is_eq(self, *sides) -> bool:
        is_eq = True
        for j in range(1, len(sides) + 1):
            if sides[0] == sides[j]:
                continue
            else:
                is_eq = False
                break
        if is_eq:
            return True
        else:
            return False

    def get_color(self) -> list:
        return self.__color

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, b, g):
            self.__color = [r, g, b]

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        rgb_list = [r, g, b]
        result = True
        for i in rgb_list:
            if 0 <= i <= 255:
                pass
            else:
                result = False
                break
        return result

    def __is_valid_sides(self, *new_sides) -> bool:
        is_int = True
        long = 0
        for item in new_sides:
            long += 1
            if isinstance(item, float):
                is_int = False
                break
        if is_int and long == self.sides_count:
            return True
        else:
            return False

    # метод проверяет является ли класс создаваемого объекта классом равносторонней фигуры
    def __is_equilateral(self):
        if self.is_equilateral:
            return True
        else:
            return False

    def get_sides(self) -> list:
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self) -> int:
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *sides):
        Figure.__init__(self, color, *sides)
        self.__radius: float = self.get_radius()

    def get_square(self) -> float:
        return 3.14 * (self.__radius ** 2)

    def get_radius(self) -> float:
        l: int = self.get_sides()[0]
        p: float = 3.14 * 2
        return l / p


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):
        Figure.__init__(self, color, *sides)
        self.__type: str == self.triangle_type(*sides)

    def get_square(self) -> float:
        p = self.__len__()/ 2
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        return sqrt(p * (p - a) * (p - b) * (p - c))

    def triangle_type(self, *sides):
        sides_list = list(sides)
        sides_list.sort()
        c = sides_list.pop()        # наибольшая сторона треугольника
        sum_ = sides_list[0] ** 2 + sides_list[1] ** 2
        # проверка и возвращение вида треугольника
        if sum_ == c ** 2:          # прямоугольный
            return 'right-angled'
        elif sum_ < c ** 2:         # тупоугольный
            return 'obtuse-angled'
        else:
            return 'acute-angled'   # остроугольный


class Cube(Figure):
    sides_count = 12
    is_equilateral = True

    def __init__(self, color, *sides):
        Figure.__init__(self, color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

