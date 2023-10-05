# Задание №3
# 📌 Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv
my_dict = {}

new_json = json.dumps(my_dict)

def my_json(my_dict):

    id = 4
    while True:
        id += 1
        name = input('Введите имя ')
        if name == 'exit':
            break
        level = input('Введите уровень ')
        if int(level) < 0 and int(level) >7:
            print('Error')
        if level not in my_dict.keys():
            my_dict[level] = {}
        my_dict[level][id] = name
        print(my_dict)

with open('new_file.json', 'r', encoding='utf=8') as f:
    my_dict = json.load(f)


my_json(my_dict)


with open('new_file.csv', 'w', encoding='utf=8', newline='') as f:
    dict_csv = csv.DictWriter(f, fieldnames=['level', 'id', 'Name'], dialect='excel-tab')
    dict_csv.writeheader()
    dict_csv.writerows(my_dict)