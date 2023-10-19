class Person:
    max_up = 3
    
    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.name = }, {p1.race = }')
print(f'{p2.name = }, {p2.race = }')
print(f'{p3.name = }, {p3.race = }')


# Параметр self и передача аргументов в экземпляр

# Первый параметр функции всегда self — указатель экземпляру на самого себя
# ● Первый параметр функции всегда self — указатель экземпляру на самого себя
# ● Параметры метода __init__ попадают в экземпляр при создании
# ● Обращение к атрибутам экземпляра происходит через self.name