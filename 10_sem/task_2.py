"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, length=1, width=None):
        self.length = length
        self.width = length if width is None else width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.length * self.width


if __name__ == "__main__":
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(6, 10)
    rect3 = Rectangle(8)
    print(
        f"Периметр прямоугольника:\n rect1 = {round(rect1.perimeter(), 2)}\n rect2 = {round(rect2.perimeter(), 2)}\
        \n rect3 = {round(rect3.perimeter(), 2)}"
    )
    print(
        f"Площадь прямоугольника:\n rect1 = {round(rect1.square(), 2)}\n rect2 = {round(rect2.square(), 2)}\
        \n rect3 = {round(rect3.square(), 2)}"
    )