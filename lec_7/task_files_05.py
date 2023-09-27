# ➢ 'strict' — вызывает исключение ValueError в случае ошибки. Работает как
# значение по умолчанию.
# ➢ 'ignore' — игнорирует ошибки кодирования. При этом игнорирование ошибок
# может привести к потере данных.
# ➢ 'replace' — вставляет маркер замены (например, '?') там, где есть
# некодируемые данные.
# ➢ 'namereplace' — при записи заменяет неподдерживаемые символы
# последовательностями \N{...}.

f = open('data.txt', 'wb')
f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()

# f = open('data.txt', 'r', encoding='utf-8')  
# print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
# f.close()

f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()

# newline — отвечает за преобразование окончания строки
# closefd — указывает оставлять ли файловый дескриптор открытым при закрытии файла
# opener — позволяет передать пользовательскую функцию для открытия файла.