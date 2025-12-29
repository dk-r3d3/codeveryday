"""
генераторы — специальные объекты, которые по требованию генерируют элементы последовательности.
задачи:
 Снижение нагрузки на память.
 Работа с бесконечными последовательностями.
 Оптимизация кода.
 В Python генератор можно создать двумя способами:
1.   С помощью функции с yield.
2.   С помощью генераторного выражения.
"""
import time
import timeit


# с помощью функции
def simple_generator():
    yield 1
    yield 2


gen = simple_generator()
print(next(gen))
print(next(gen))

# для получения всех значений, но еслив  памяти уже вызывался, то осатвшиеся значения покажет
print(f"Все значения генератора: {list(gen)}")
# с помощью генераторного выражения
"""
(expression for item in iterable if condition)
expression — что делать с каждым элементом;
item — переменная для текущего элемента;
iterable — последовательность (например, список, кортеж, диапазон);
if condition (необязательно) — фильтр для выбора элементов.
"""
gen_exp = (x for x in range(5))  # круглые скобки вместо []
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))
print("\n\n")

"""Тестирование list comprehension vs generator expression"""
list_comprehension = 'sum([i**2 for i in range(10000)])'
list_comprehension_time = timeit.timeit(list_comprehension, number=1000)
print(f'list_comprehension time - {list_comprehension_time}')

generator_expression = 'sum(i**2 for i in range(10000))'
generator_expression_time = timeit.timeit(generator_expression, number=1000)
print(f'generator_expression time - {generator_expression_time}')
