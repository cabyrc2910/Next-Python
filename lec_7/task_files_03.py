# ● Режимы работы с файлами
# Рассмотрим доступные режимы работы с файлами.
# ➢ 'r' — открыть для чтения (по умолчанию)
# ➢ 'w' — открыть для записи, предварительно очистив файл
# ➢ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже
# существует
# ➢ 'a' — открыть для записи в конец файла, если он существует
# ➢ 'b' — двоичный режим
# ➢ 't' — текстовый режим (по умолчанию)
# ➢ '+' — открыты для обновления (чтение и запись)

# ● Метод close()
# После завершения работы с файлом необходимо освободить ресурсы. Для этого
# вызывается метод close().

f = open('text_data.txt', 'a', encoding='utf-8')
f.write('Окончание файла\n')
f.close()