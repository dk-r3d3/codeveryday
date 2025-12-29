"""
Написать свой класс-итератор и генератор для последовательности Fibonacci
Все генераторы - итераторы, но не все итераторы - генераторы
"""
import timeit


def fib_iterator_while(n):
    res = []
    var1 = 0
    var2 = 1
    sum = 0
    count = 0
    while count != n:
        res.append(sum)
        var1 = var2
        var2 = sum
        sum = var1 + var2
        count += 1
    return res


# print(fib_iterator_while(5))
execution_time = timeit.timeit(lambda: fib_iterator_while(500), number=1000)
print(f"fib_iterator_while - {execution_time}")


def fib_iterator_for(n):
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


# print(fib_iterator_for(500))
execution_time = timeit.timeit(lambda: fib_iterator_for(500), number=1000)
print(f"fib_iterator_for - {execution_time}")


def feb_generator(n):
    var1 = 0
    var2 = 1
    sum = 0
    count = 0
    while count != n:
        yield sum
        var1 = var2
        var2 = sum
        sum = var1 + var2
        count += 1


res_gen = feb_generator(500)
# print(list(res_gen))
# print(next(res_gen))
# print(next(res_gen))
# print(next(res_gen))
execution_time = timeit.timeit(lambda: list(res_gen), number=1000)
# print(f"feb_generator - {execution_time}")


def generator_usage():
    """Тестируем только извлечение данных из готового генератора."""
    total_time = 0

    for _ in range(1000):
        # Каждый раз НОВЫЙ генератор
        gen = feb_generator(500)

        # Измеряем только извлечение
        start = timeit.default_timer()
        list(gen)  # Извлекаем все элементы
        total_time += timeit.default_timer() - start

    return total_time


print(f"Только использование 1000 раз: {generator_usage():.4f} сек")