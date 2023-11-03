# Задание №4
# 📌 Доработаем класс Архив из задачи 2.
# 📌 Добавьте методы представления экземпляра для программиста и для пользователя.

class Arche:
    '''Doc for class Arch. '''
    number = []
    my_str = []

    def __new__(cls, num, my_str):
        instance = super().__new__(cls)
        instance.number.append(num)
        instance.my_str.append(my_str)
        return instance

    def __str__(self):
        return f'This is str {self.number = } {self.my_str = }'

    def __repr__(self):
        return f'It"s repr {self.number} {self.my_str}'

arch1 = Arche(10, '2023')
arch2 = Arche(20, 'October')
arch3 = Arche(30, '18')

print(arch1.number, arch1.my_str)
# help(arch1)
print(repr(arch1))
print(f'{arch1}')
print(f'{arch1 = }')