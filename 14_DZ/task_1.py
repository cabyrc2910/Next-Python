"""
Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.

Используйте модуль doctest.

Тесты:
test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с шириной 5 и r4 с отрицательной шириной (-2).
Убедимся, что r1.width корректно установлен на 5, а создание r4 вызывает исключение NegativeValueError.

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники r2 с шириной 3 и высотой 4. Проверяем,
что r2.width равно 3 и r2.height равно 4.

test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.perimeter()
возвращает 20. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter() возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5 и проверяем, что r1.area() возвращает
25. Также создан прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4
Выполняем операцию сложения r1 + r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и
высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с шириной 5 и r2 с шириной 3 и высотой 4.
Выполняем операцию вычитания r1 - r2 и проверяем, что полученный прямоугольник r3 имеет правильные значения ширины
и высоты (2 и 2.0 соответственно).

Запускать тесты не надо, автотест это сделает сам:

__file__ = None
doctest.testmod(extraglobs={'__file__': __file__})

"""


import doctest


class Rectangle:
    """
    Класс, представляющий прямоугольник.
    """

    def __init__(self, width, height=None):
        """
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r2 = Rectangle(-2)
        Traceback (most recent call last):
            ...
        ValueError: Negative value for width is not allowed
        >>> r3 = Rectangle(3, 4)
        >>> r3.width
        3
        >>> r3.height
        4
        """
        if width < 0:
            raise ValueError("Negative value for width is not allowed")
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        """
        return self.width * self.height

    def __add__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r1 < r2
        False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r1 == r2
        False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r1 <= r2
        False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        >>> r1 = Rectangle(5)
        >>> print(r1)
        Прямоугольник со сторонами 5 и 5
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        >>> r1 = Rectangle(5)
        >>> repr(r1)
        'Rectangle(5, 5)'
        """
        return f"Rectangle({self.width}, {self.height})"


if __name__ == "__main__":
    doctest.testmod(extraglobs={"__file__": None})