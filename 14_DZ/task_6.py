"""
У вас есть два класса: Person и Employee из предыдущих задач.
Необходимо написать тесты с использованием модуля pytest и лежать в class TestEmployee.
*Тесты необходимо написать именно в этом порядке!

Тесты:

test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan",
отчеством "Ivanovich" и убедитесь, что метод full_name() возвращает правильное полное имя в формате "Ivanov Ivan
Ivanovich".

test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с возрастом 30, вызовите метод birthday
() и убедитесь, что возраст увеличился на 1 и стал равным 31.

test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с зарплатой 50000, вызовите
метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.

test_employee_str: Тестирование метода __str__(). Создайте объект Employee с данными: фамилия "Ivanov", имя "Ivan",
отчество "Ivanovich", возраст 30, должность "manager" и зарплата 50000. Убедитесь, что метод __str__() возвращает
правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".

test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией "Ivanov" и
убедитесь, что атрибут last_nameвозвращается в верхнем регистре, то есть "Ivanov".

Запускать тесты не надо, автотест это сделает сам:

# Запускаем pytest.main() с нужными параметрами
    pytest.main(["--no-header", '-q', "--durations=0", new_filename])

На выходе после автоматической обрезки информации в тестах вы должны получить:

..F..                                                                    [100%]

"""
import pytest


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= 1 + percent / 100

    def __str__(self):
        return f"{self.full_name()} ({self.position})"


# Введите ваше решение ниже
class TestEmployee:
    @pytest.fixture
    def data(self):
        emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
        return emp

    def test_employee_full_name(self, data):
        assert data.full_name() == "Ivanov Ivan Ivanovich"

    def test_employee_birthday(self, data):
        data.birthday()
        assert data.get_age() == 31

    def test_employee_raise_salary(self, data):
        data.raise_salary(10)
        assert data.salary == 55000.0

    def test_employee_str(self, data):
        assert str(data) == "Ivanov Ivan Ivanovich (Manager)"

    def test_employee_last_name_title(self, data):
        assert data.last_name == "Ivanov".title()


"""!!!"""
# # Проверка автотеста с моим ответом

# import warnings

# warnings.filterwarnings("ignore")

# import pytest


# class Person:
#     def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
#         self.last_name = last_name.title()
#         self.first_name = first_name.title()
#         self.patronymic = patronymic.title()
#         self._age = age

#     def full_name(self):
#         return f"{self.last_name} {self.first_name} {self.patronymic}"

#     def birthday(self):
#         self._age += 1

#     def get_age(self):
#         return self._age


# class Employee(Person):
#     def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
#         super().__init__(last_name, first_name, patronymic, age)
#         self.position = position.title()
#         self.salary = salary

#     def raise_salary(self, percent: float):
#         self.salary *= 1 + percent / 100

#     def __str__(self):
#         return f"{self.full_name()} ({self.position})"


# # Введите ваше решение ниже
# class TestEmployee:
#     @pytest.fixture
#     def data(self):
#         emp = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
#         return emp

#     def test_employee_full_name(self, data):
#         assert data.full_name() == "Ivanov Ivan Ivanovich"

#     def test_employee_birthday(self, data):
#         data.birthday()
#         assert data.get_age() == 31

#     def test_employee_raise_salary(self, data):
#         data.raise_salary(10)
#         assert data.salary == 55000.0

#     def test_employee_str(self, data):
#         assert str(data) == "Ivanov Ivan Ivanovich (Manager)"

#     def test_employee_last_name_title(self, data):
#         assert data.last_name == "Ivanov".title()


# import os
# import sys

# # Текущее имя файла
# current_filename = __file__

# # Новое имя файла с добавлением "test_" в начале
# new_filename = "test_1.py"
# # + os.path.basename(current_filename))

# # Откройте текущий файл для чтения
# with open(current_filename, "r") as source_file:
#     source_code = source_file.read()
#     source_file.close()

# # Запишите код в новый файл
# with open(new_filename, "w") as new_file:
#     new_file.write(source_code)
#     new_file.close()

# with open(new_filename, "r") as new_file:
#     file_contents = new_file.read()
#     # Выводим содержимое файла на экран
#     # print(file_contents)


# # Открываем файл для записи
# with open("pytest_output.txt", "w") as file:
#     # Перенаправляем stdout в файл
#     sys.stdout = file

#     # Запускаем pytest.main() с нужными параметрами
#     pytest.main(["--no-header", "-q", "--durations=0", new_filename])

# # Возвращаем stdout в исходное состояние
# sys.stdout = sys.__stdout__
# # Считываем содержимое файла
# with open("pytest_output.txt", "r") as file:
#     lines = file.readlines()
#     first_line = file.readline()
#     first_n_lines = lines[:1]

# # Выводим первые 5 строк
# for line in first_n_lines:
#     print(line)