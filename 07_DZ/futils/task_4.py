# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import random
import string
import shutil

def maker(extension, file_amount=42, dir=".", name_min=6, name_max=30, bytes_min=256, bytes_max=4096):
    """
    Create random_name.extension with random bytes inside
    ARGS: 
    - extension
    - name_min
    - name_max
    - content_min
    - content_max
    -files
    """
    if not shutil.os.path.exists(dir):
        shutil.os.mkdir(dir) 
    for _ in range(file_amount):  
        name = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(name_min, name_max))
        bytes = random.randbytes(random.randint(bytes_min, bytes_max))
        with open(f"{dir}/{name}.{extension}", 'xb')as f:
            f.write(bytes)