# Задание №3
# 📌 Добавьте к задачам 1 и 2 строки документации для классов.

import time

class MyStr(str):
    '''Doc for class MyStr. Extended string'''
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        # instance.value = value
        instance.name = name
        instance.time = time.time()
        return instance

        # def __init__(self, value, name) -> None:
        # super().__init__(value)
        # self.name = name
        # self.time = time.time()


sss = MyStr('Hello World', 'Athor')

print(sss)
print(sss.name)
print(sss.time)
print(sss.upper())
help(sss )