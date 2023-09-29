import os
import shutil


def sort_files_by_type(src_dir, dest_dir):
    try:
        # Попытка получить список файлов в исходной директории
        files = os.listdir(src_dir)
    except FileNotFoundError:
        print(f"Папка '{src_dir}' не существует.")
        return

    # Создаем словарь для соответствия расширений файлов и их типов
    file_types = {
        "видео": [".mp4", ".avi", ".mkv"],
        "изображения": [".jpg", ".jpeg", ".png", ".gif"],
        "текст": [".txt", ".pdf", ".doc", ".docx"],
    }

    # Создаем папки для каждого типа файлов в целевой директории
    for type_dir in file_types:
        os.makedirs(os.path.join(dest_dir, type_dir), exist_ok=True)

    for file in files:
        file_extension = os.path.splitext(file)[-1].lower()
        moved = False

        for file_type, extensions in file_types.items():
            if file_extension in extensions:
                src_file = os.path.join(src_dir, file)
                dest_file = os.path.join(dest_dir, file_type, file)
                shutil.move(src_file, dest_file)
                moved = True
                break

        if not moved:
            # Файл не подошел для сортировки, оставляем его в исходной папке
            print(f"файл не подошел для сортировки: {file}")
            continue


# Пример использования функции
if __name__ == "__main__":
    source_directory = "./Users/Иван/Desktop/GeekBrains/16. Next-Python/07_DZ/1.py/original"
    destination_directory = "./Users/Иван/Desktop/GeekBrains/16. Next-Python/07_DZ/1.py/"
    sort_files_by_type(source_directory, destination_directory)