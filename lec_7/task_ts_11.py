# ● Переименование файлов
# Переименование файла подразумевает сохранение неизменным файла в файловой таблице и в содержимом файла, но изменение его имени. Для переименования можно воспользоваться следующим кодом.

import os
from pathlib import Path

os.rename('old_name.py', 'new_name.py')

p = Path('old_file.py')
p.rename('new_file.py')

Path('new_file.py').rename('newest_file.py')