# Задание №6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения

class Rectangle:
    def __init__(self, len_rec, width = None):
        self.len_rec = len_rec
        if width is None:
            self.width = len_rec
        else:
            self.width = width

    def perimeter(self):
        return 2 * (self.len_rec + self.width)

    def square(self):
        return self.len_rec * self.width

    def __add__(self, other):
        return Rectangle(self.len_rec + other.len_rec, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(abs(self.len_rec - other.len_rec), abs(self.width - other.width))

    def __eq__(self, other):
        return self.square() == other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __ne__(self, other):
        return self.square() != other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __gt__(self, other):
        return self.square() > other.square()

p1 = Rectangle(4, 5)
p2 = Rectangle(40, 50)

print(round(p1.perimeter(), 2))
print(round(p1.square(), 2))
print(round(p2.perimeter(), 2))
print(round(p2.square(), 2))

p3 = p1 + p2
print(f'{p3.len_rec = }, {p3.width = }')
print(p3.perimeter())
print(round(p3.square(), 2))

p4 = p1 - p2
print(f'{p4.len_rec = }, {p4.width = }')
print(p4.perimeter())
print(round(p4.square(), 2))

print( p3 < p4) 