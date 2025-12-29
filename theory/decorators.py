"""
Декораторы - функции обертки для функций и классов
"""
import time


def timer(func):
    """Декоратор для измерения врмени работы функции"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        res_time = end_time - start_time
        print(f"Алгоритм выполнился за {res_time: .10f} сек")
        return result
    return wrapper


def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:

                    return f"Алгоритм без ошибок сработал \n{func(*args, **kwargs)}"

                except Exception as e:
                    print(f"Попытка №{attempt + 1}, ошибка - {e}")
                    if attempt < max_attempts - 1:
                        print(f"Waiting {delay} sec...")
                        time.sleep(delay)
                    else:
                        print(f"All {max_attempts} attempts failed!")
                        raise e

            return None
        return wrapper
    return decorator

# пример

@retry(3, 1)
@timer
def fib_iterator_for(n):
    """Послед. Фиббоначи"""
    res = []
    var1 = 0
    var2 = 1
    sum = 0
    for i in range(n):
        res.append(sum)
        var1 = var2
        var2 = sum
        sum = var1 + var2
    return res

print(fib_iterator_for(12))