# Задание №3
# 📌 Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import csv
import json
from sys import argv

if __name__ == "__main__":
    if len(argv) < 3:
        print(f"Example: python {argv[0]} input.json output.csv")

def csv_gen(json_file, csv_file):
    """
    Description: Function creates csv file from custom nested csv file
    Arguments:
        json_file - string output json file name
        csv_file - string input csv file name
    Returns: String message
    """
    with open(json_file, 'r', encoding='utf-8') as input_file, open(csv_file, 'w', newline='', encoding='utf-8') as output_file:
        json_data = json.load(input_file)
        # Убираем вложенность словарей
        flattened_data = []
        for key, value in json_data.items():
            for sub_key, sub_value in value.items():
                flattened_data.append({"level": key, "id": sub_key, "name": sub_value})

        fieldnames = ["level", "id", "name"]
        csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        csv_writer.writeheader()  # заголовок
        csv_writer.writerows(flattened_data)

    return f"{csv_file} successfully created/updated."


if __name__ == '__main__':
    csv_gen(argv[1], argv[2])