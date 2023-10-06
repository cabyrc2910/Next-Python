# Задание
# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import shutil
import json
import csv
import pickle
from sys import argv

if __name__ == '__main__':
    if len(argv) < 2:
        argv.append(".")

def dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in shutil.os.walk(directory):
        for filename in filenames:
            filepath = shutil.os.path.join(dirpath, filename)
            total_size += shutil.os.path.getsize(filepath)
    return total_size

def ls_dir(dirname):
    """
    Function: Creates 3 files (json, csv, pickle) containing given directory and file info.
    Arguments:
        string dirname
    Returns: string message
    """
    ls = []
    root = shutil.os.walk(dirname)
    for i in root:    
        dir = i[0]
        parent = shutil.os.path.dirname(i[0])
        size = dir_size(dir)
        ls.append({"name":dir, "parent":parent, "type":"directory", "size":size})
        files = i[2]
        for file in files:
            filepath = shutil.os.path.join(dir, file)
            size = shutil.os.path.getsize(filepath)
            ls.append({"name":file, "parent":parent, "type":"file", "size":size})
    with open('task01.json', 'w', encoding='utf-8') as f:
        json.dump(ls, f, ensure_ascii=False, indent=2)
    with open('task01.csv', 'w', encoding='utf-8', newline="") as f:        
        csv_writer = csv.DictWriter(f, [i for i in ls[0]])
        csv_writer.writeheader()  
        csv_writer.writerows(ls)
    with open('task01.pickle', "wb") as f:
        pickle.dump(ls, f)
    return "Created/updated: task01.json, task01.csv, task01.pickle"

if __name__ == '__main__':
    dirname = argv[1]
    ls_dir(dirname)