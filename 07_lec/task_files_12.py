# ● Чтение методом readline - для чтения текстового файла построчно

with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
       print(res)