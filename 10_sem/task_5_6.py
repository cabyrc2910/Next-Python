"""
N5
Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

N6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def my_ptint(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Вес: {self.weight}.кг"


class Cat(Animal):
    def __init__(self, name, age, weight, breed) -> None:
        super().__init__(name, age, weight)
        self.breed = breed

    def my_ptint(self):
        return f"{super().my_ptint()} Порода: {self.breed}"


class Birth(Animal):
    def __init__(self, name, age, weight, wings) -> None:
        super().__init__(name, age, weight)
        self.wings = wings

    def my_ptint(self):
        return f"{super().my_ptint()} Размах крыльев: {self.wings}"


if __name__ == "__main__":
    cat1 = Cat("Tima", 2, 11, "maine coon")
    birth1 = Birth("Gosha", 4, 3, 0.5)
    print(cat1.my_ptint())
    print(birth1.my_ptint())