# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import pathlib

def sorter(dirname):
    file_list = {}

    # Создаем папки, если они не существуют
    for folder in ["video", "img", "text"]:
        folder_path = pathlib.Path(dirname) / folder
        folder_path.mkdir(exist_ok=True)

    # Перемещаем файлы в соответствующие папки
    for file_path in pathlib.Path(dirname).glob("*"):
        if file_path.is_file():
            if file_path.suffix == ".avi":
                dest_folder = "video"
            elif file_path.suffix == ".jpg":
                dest_folder = "img"
            elif file_path.suffix == ".txt":
                dest_folder = "text"
            else:
                continue  # Пропускаем файлы, которые не подходят под расширения

            dest_path = pathlib.Path(dirname) / dest_folder / file_path.name
            file_path.rename(dest_path)

    # Собираем список файлов в каждой папке
    return list(pathlib.os.walk(dirname))[1:]


if __name__ =='__main__':
    print(*filter(avi=2, jpg=2, txt=2, dir='tmp'), sep="\n")
    print(*sorter("tmp"), sep="\n")