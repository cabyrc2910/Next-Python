# Задание №4    
"""
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
● возврат строки без изменений
● возврат строки с преобразованием регистра без потери символов
● возврат строки с удалением знаков пунктуации
● возврат строки с удалением букв других алфавитов
● возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import pytest


def test_no_chenge():
    assert func_clear_text("hello world") == "hello world"


def test_lower():
    assert func_clear_text("Hello world") == "hello world"


def test_punctuation():
    assert func_clear_text("Hello world,") == "hello world"


def test_other_alphabets():
    assert func_clear_text("Hello worldПривет,") == "hello world"


def test_all_above_points():
    assert func_clear_text("Hello, world_Привет,") == "hello world"


def func_clear_text(text: str) -> str:
    new_text = "".join(
        letter for letter in text if 97 <= ord(letter) <= 122 or 65 <= ord(letter) <= 90 or letter == " "
    )
    return new_text.lower()


if __name__ == "__main__":
    pytest.main([f"{__file__}", "-v"])
