# Если необходимо удалить каталог со всем его содержимым (вложенные каталоги и файлы), подойдёт функция из модуля shutil

import shutil

shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')