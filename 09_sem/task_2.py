# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.

from typing import Callable
from random import randint as rnd

def my_fun(func_1: Callable):
    def wrapper(enigma2, num_try2):
        if not 1 <= enigma2 <= 100:
            enigma2 = rnd(1, 100)
        if not 1 <= num_try2 <= 10:
            num_try2 = rnd(1, 10)
        return func_1(enigma2, num_try2)
    return wrapper


@my_fun
def new_fun(enigma: int, num_try: int):
    for _ in range(num_try):
        my_answer = int(input('Введите число: '))
        if my_answer > enigma:
            print('Меньше')
        elif my_answer < enigma:
            print('Больше')
        else:
            print('Верно')
            break


if __name__ == '__main__':

    # hello = my_fun(30, 7)
    # print(hello)
    new_fun(34, 5)