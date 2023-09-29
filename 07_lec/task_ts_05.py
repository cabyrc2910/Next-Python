# ● Удаление каталогов
# Для удаления одного каталога подойдут следующие функция и метод

import os
from pathlib import Path

# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()