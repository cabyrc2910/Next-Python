# Допустимые типы данных для преобразования
# ● None, True и False;
# ● int, float, complex;
# ● str, bytes, bytearrays;
# ● tuple, list, set, dict если они содержат объекты, обрабатываемые pickle;
# ● встроенные функции и функции созданные разработчиком и доступные из верхнего уровня модуля, кроме lambda функций;
# ● классы доступные из верхнего уровня модуля;
# ● экземпляры классов, если pickle смог обработать их дандер __dict__ или результат вызова метода __getstate__().

# Сериализация

# ● pickle.dump(my_dict, f)
# сохранение объекта в бинарном файле
# ● result = pickle.dumps(my_dict)
# сохранение объекта в строку байт

import pickle
18
my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
    "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
print(my_dict)
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')