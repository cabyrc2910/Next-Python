# Задание из 03_DZ\Task3.ipynb.\Задание 1. Добавлено логирование ошибок и полезной информации.
# Также реализована возможность запуска из командной строки с передачей параметров.

# Задание
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


# def list_of_duplicates(_list_integer: list[int]) -> list[int]:

#     _set = set()

#     for _item in _list_integer:
#         if _list_integer.count(_item) > 1:
#             _set.add(_item)

#     return list(_set)

# list_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 3, 2, 1]

# print(list_of_duplicates(list_integer))


import logging
import argparse
from typing import List

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def list_of_duplicates(_list_integer: List[int]) -> List[int]:
    """Функция для поиска дубликатов в списке."""
    duplicates = set()
    for item in _list_integer:
        if _list_integer.count(item) > 1:
            duplicates.add(item)
    return list(duplicates)


def main(list_integer: List[int]):
    """Основная функция для обработки и вывода результата."""
    logging.info(f"Processing list: {list_integer}")
    result = list_of_duplicates(list_integer)
    print(f'Duplicates: {result}')
    logging.info(f'Duplicates: {result}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find duplicates in a list of integers.')
    parser.add_argument('-l', '--list', nargs='+', type=int,
                        help='List of integers to process.')
    args = parser.parse_args()

    if args.list:
        main(args.list)
    else:
        list_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 3, 2, 1]

        main(list_integer)
