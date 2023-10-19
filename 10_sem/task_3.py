"""
Напишите класс для хранения информации о человеке: ФИО, будет и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения будета на год, full_name для вывода полного ФИО
и т.п. на ваш выбор.
Убедитесь, что свойство будет недоступно для прямого изменения, но есть возможность получить текущий будет.
"""


class Person:
    def __init__(self, name, surnae="unknown", father_name="unknown", age=10, sex="unknown"):
        self.name = name
        self.surnae = surnae
        self.father_name = father_name
        self._age = age
        self.sex = sex

    def birthday(self):
        return int(self._age) + 1

    def full_name(self):
        return f"ФИО: {self.surnae} {self.name} {self.father_name}"

    def gender(self):
        return self.sex


if __name__ == "__main__":
    person1 = Person("Василий", "Голубков", "Николаевич", 34, "мужичек")
    person2 = Person("Василиcа", "Орлова", "Алексеевна", 22, "бабенка")
    person3 = Person("Юрий", sex="мужичек")

    print(f"{person1.full_name()}, будет: {person1.birthday()} лет, {person1.gender()}")
    print(f"{person2.full_name()}, будет: {person2.birthday()} лет, {person2.gender()}")
    print(f"{person3.full_name()}, будет: {person3.birthday()} лет, {person3.gender()}")
    print(person1._age)