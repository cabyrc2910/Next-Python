# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

import os
import random
import string


def create_random_files(
    folder_path,
    extension,
    min_name_length=6,
    max_name_length=30,
    min_size=256,
    max_size=4096,
    num_files=42,
):
    if not extension.startswith("."):
        extension = f".{extension}"

    # Создаем папку, если она не существует
    os.makedirs(folder_path, exist_ok=True)

    for _ in range(num_files):
        # Генерируем случайное имя файла
        name_length = random.randint(min_name_length, max_name_length)
        file_name = (
            "".join(random.choice(string.ascii_letters + string.digits) for _ in range(name_length))
            + extension
        )

        # Собираем полный путь к файлу
        file_path = os.path.join(folder_path, file_name)

        # Генерируем случайное количество байт данных
        size = random.randint(min_size, max_size)
        data = os.urandom(size)

        # Создаем файл и записываем в него данные
        with open(file_path, "wb") as file:
            file.write(data)


def generate_files_with_extensions(extension_info):
    for extension, num_files in extension_info.items():
        folder_path = f"./Seminars/Seminar7/task05/{extension}"
        create_random_files(folder_path, extension, num_files=num_files)


if __name__ == "__main__":
    extension_info = {
        ".txt": 20,  # 20 файлов с расширением .txt
        ".jpg": 10,  # 10 файлов с расширением .jpg
        ".doc": 5,  # 5 файлов с расширением .doc
    }
    generate_files_with_extensions(extension_info)