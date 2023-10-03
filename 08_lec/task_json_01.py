# ● Преобразование JSON в Python
# Договоримся, что представленный выше объект JSON сохранён в виде текстового
# файла user.json в кодировке UTF-8 в той же директории, что и исполняемый код.

# Функция load загрузила объект из файла и произвела его десериализацию —
# превращение в словарь dict. Дальнейшие манипуляции со словарём не вызовут
# затруднений у Python разработчиков.

# ● json_file = json.load(f)
# загрузка JSON из файла и сохранение в dict или list
# ● json_list = json.loads(json_text)
# загрузка JSON из строки и сохранение в dict или list

import json

with open('user.json', 'r', encoding='utf-8') as f:
    json_file = json.load(f)
    
print(f'{type(json_file) = }\n{json_file = }')
print(f'{json_file["name"] = }')
print(f'{json_file["address"]["geo"] = }')
print(f'{json_file["email"] = }')