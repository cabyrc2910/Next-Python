import time
from typing import Callable
from functools import wraps


def count(num: int = 1):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result
        
        return wrapper
    
    return deco


@count(10)
def factorial(n: int) -> int:
    """Return the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(1000) = }')
print(f'{factorial.__name__ = }')
help(factorial)  

# Декоратор wraps добавляется к функции wrapper, т.е. к самой глубоко вложенной функции. 
# В качестве аргумента wraps должен получить параметр декларируемой функции. 
# Теперь factorial возвращает свои название и строку документации.