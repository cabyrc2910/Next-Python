"""
Создайте класс окружность. Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""
from math import pi


class Circle:
    def __init__(self, radius=1) -> None:
        self.radius = radius

    def circ_len(self):
        return 2 * pi * self.radius

    def cir_rad(self):
        return pi * self.radius**2


if __name__ == "__main__":
    cir1 = Circle(4)
    cir2 = Circle(6)
    cir3 = Circle(8)
    print(
        f"Длинна окружности:\n cir1 = {round(cir1.circ_len(), 2)}\n cir2 = {round(cir2.circ_len(), 2)}\
        \n cir3 = {round(cir3.circ_len(), 2)}"
    )
    print(
        f"Площадь окружности:\n cir1 = {round(cir1.cir_rad(), 2)}\n cir2 = {round(cir2.cir_rad(), 2)}\
        \n cir3 = {round(cir3.cir_rad(), 2)}"
    )