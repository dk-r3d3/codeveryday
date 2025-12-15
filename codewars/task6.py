"""
Напишите функцию persistence, которая принимает положительный параметр num и возвращает
его мультипликативную устойчивость, то есть количество раз, которое нужно умножить на цифры в num,
чтобы получить однозначное число.

Например (Входные данные —> Выходные данные):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
"""
import math


def persistence(n):
    if n < 10:
        return 0
    count = 1
    res = math.prod([int(i) for i in str(n)])
    while res // 10 >= 1:
        res = math.prod([int(i) for i in str(res)])
        count += 1
    return count

print(persistence(39))
print(persistence(999))
print(persistence(4))