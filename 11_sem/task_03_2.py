# Задание №3
# 📌 Добавьте к задачам 1 и 2 строки документации для классов.

class Arche:
    '''Doc for class Arch.'''
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
help(arch1)