"""
Дополните функцию scramble(str1, str2), которая возвращает true, если часть str1 символов можно переставить так,
чтобы получилось str2, в противном случае возвращается false.

Примечания:

Будут использоваться только строчные буквы (a-z). Знаки препинания и цифры не допускаются.
Необходимо учитывать производительность.
Примеры
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""
from collections import Counter  # позволяет определить, сколько раз встречается каждый элемент в последовательности


def scramble(s1, s2):
    # стопудово надо использовать Counter
    # Сравнение наборов данных
    diff = Counter(s2) - Counter(s1)
    if diff:
        return False
    else:
        return True
    # """Говнокод"""
    # dict = {}
    #
    # for i in s2:
    #     if i in dict.keys():
    #         dict[i] += 1
    #     elif i in s1:
    #         dict[i] = 1
    # """
    # Если вам необходимо проверить, все ли значения в данном словаре оцениваются как истинные.
    # В этом случае вы можете использовать .values():
    # """
    # has_greater = any(value > 1 for value in dict.values())  # проверяем, есть ли хоть одно значение больше 1
    #
    # if len(dict) >= len(s2) or has_greater:
    #     return all(dict.values())
    # elif len(dict) < len(s2) and not has_greater:
    #     return False  # проверили на случай,  если одинаковые значения несколько раз повторяются


print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble("scriptjava", "javascript"))
print(scramble("tybzsdzigurgk", "gisgdydbr"))
print(scramble("wsiwahurqdapgasx", "ssidpaquriw"))