# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import shutil

def filer(**kwargs) -> list:
    dir=kwargs.pop("dir")
    for k, v in kwargs.items():
        maker(k, v, dir)
    return list(shutil.os.walk(dir))[0][2]