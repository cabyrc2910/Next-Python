# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# 📌 list-архивы также являются свойствами экземпляра

class Arche:
    number = []
    my_str = []

    def __new__(cls, num, my_str):
        instance = super().__new__(cls)
        instance.number.append(num)
        instance.my_str.append(my_str)
        return instance

arch1 = Arche(10, '2023')
arch2 = Arche(20, 'October')
arch3 = Arche(30, '18')

print(arch1.number, arch1.my_str)