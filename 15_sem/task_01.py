# Задание №1
# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.

import logging


logging.basicConfig(filename='mylog.log', filemode='a', encoding='utf-8', level=logging.ERROR)


def dev_2_number(a, b):
    try:
        res = a / b
    except ZeroDivisionError as err:
        logging.error(f'{err}, {a} , {b}')
        res = None
    return res


print(dev_2_number(5, 0))