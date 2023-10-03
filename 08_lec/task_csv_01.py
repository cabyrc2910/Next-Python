# ● Чтение CSV
# Функция csv.reader принимает на вход файловый дескриптор и построчно читает информацию.

# ● with open('biostats.csv', 'r', newline='') as f:
# параметр newline='' для работы с CSV
# ● csv_file = csv.reader(f)
# csv_file позволяет построчно читать csv файл в список list

import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    for line in csv_file:
        print(line)
    print(type(line))
    
# 🔥 Важно! При работе с CSV необходимо указывать параметр newline=’’ во
# время открытия файла.