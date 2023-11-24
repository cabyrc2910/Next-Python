# Задание №2
"""
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
● возврат строки без изменений
● возврат строки с преобразованием регистра без потери символов
● возврат строки с удалением знаков пунктуации
● возврат строки с удалением букв других алфавитов
● возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""


def func_clear_text(text: str) -> str:
    """
    >>> func_clear_text('hello world')
    'hello world'
    >>> func_clear_text('Hello world')
    'hello world'
    >>> func_clear_text('Hello world,')
    'hello world'
    >>> func_clear_text('Hello worldПривет')
    'hello world'
    >>> func_clear_text('Hello, world_Привет')
    'hello world'
    """
    new_text = "".join(
        letter for letter in text if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90 or letter == " "
    )
    return new_text.lower()


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)



