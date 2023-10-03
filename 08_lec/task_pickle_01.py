# Модуль Pickle
# Модуль pickle не занимается проверкой потока байт на безопасность перед распаковкой. Не используйте его с тем набором байт, безопасность которого не можете гарантировать.



import pickle
import os

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f'{res = }')

os.system('echo Hello world!')

