# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

# Ваша задача:

# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

# Введите ваше решение ниже

class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass

class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        if not last_name:
            raise InvalidNameError(f"Invalid name: {last_name}. Name should be a non-empty string.")
        if not first_name:
            raise InvalidNameError(f"Invalid name: {first_name}. Name should be a non-empty string.")
        if not middle_name:
            raise InvalidNameError(f"Invalid name: {middle_name}. Name should be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")

        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def get_age(self):
        return self.age

    def birthday(self):
        self.age += 1


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, employee_id):
        super().__init__(last_name, first_name, middle_name, age)
        if not isinstance(employee_id, int) or employee_id < 100000 or employee_id > 999999:
            raise InvalidIdError(
                f"Invalid id: {employee_id}. Id should be a 6-digit positive integer between 100000 and 999999.")

        self.employee_id = employee_id

    def get_level(self):
        return self.employee_id % 7


#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# person = Person("", "John", "Doe", 30)
# print(person)