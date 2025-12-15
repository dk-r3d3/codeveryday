"""
Моя подруга хочет придумать новое название для своей группы.
Ей нравятся группы, которые используют формулу: «The» + существительное с заглавной буквы, например:

"dolphin" -> "The Dolphin"

Однако, когда существительное НАЧИНАЕТСЯ и ЗАКАНЧИВАЕТСЯ одной и той же буквой,
она любит повторять это существительное дважды и соединять его с помощью первой и последней буквы
в одно слово (БЕЗ артикля «the» перед ним), например так:

"alaska" -> "Alaskalaska"

Напишите функцию, которая принимает существительное в виде строки и
возвращает предпочтительное название группы в виде строки.
"""


def band_name_generator1(name):
    """АлЯ генератор"""
    if name[0] != name[len(name) - 1]:
        yield f"The {name[0].upper()}{name[1:]}"
    else:
        yield f"{name[0].upper()}{name[1:]}{name[1:]}"


def band_name_generator2(name):
    if name[0] != name[len(name) - 1]:
        return f"The {name[0].upper()}{name[1:]}"
    else:
        return f"{name[0].upper()}{name[1:]}{name[1:]}"


res1 = band_name_generator1("dolphin")
res2 = band_name_generator1("alaska")
print(next(res1))
print(next(res2))
