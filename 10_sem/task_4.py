"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""
from task03 import Person
from random import randint as rnd


class Employee(Person):
    def __init__(
        self, person_id, name, surnae="unknown", father_name="unknown", age=10, sex="unknown"
    ):
        super().__init__(name, surnae, father_name, age, sex)
        self.id = person_id
        self.access = self.get_access()

    def get_access(self):
        my_sum = sum(int(i) for i in str(self.id))
        return my_sum % 7


if __name__ == "__main__":
    emp1 = Employee(rnd(100000, 999999), "Василий", "Голубков", "Николаевич", 34, "мужичек")
    emp2 = Employee(rnd(100000, 999999), "Василиcа", "Орлова", "Алексеевна", 22, "бабенка")
    emp3 = Employee(rnd(100000, 999999), "Юрий", sex="мужичек")
    print(f" access = {emp1.access} id = {emp1.id}")
    print(f" access = {emp2.access} id = {emp2.id}")
    print(f" access = {emp3.access} id = {emp3.id}")