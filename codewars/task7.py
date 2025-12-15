"""
Ваша задача — отсортировать заданную строку. Каждое слово в строке будет содержать одно число.
Это число обозначает позицию, которую слово должно занимать в результате.

Примечание: числа могут быть от 1 до 9. Таким образом, первым словом будет 1 (а не 0).

Если входная строка пуста, верните пустую строку. Слова во входной строке будут содержать только
допустимые последовательные числа.

Примеры
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""


def order(sentence):
    res = [j for i in sentence.split() for j in i if j.isdigit()]
    my_dict = {word: int(count) for word, count in zip(sentence.split(), res)}
    sort_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    """
    Описание:
    sorted работает так - [('4of', 4), ('Fo1r', 1), ('pe6ople', 6)]
    в lambda  мы говорим, чтобы брал не ключ-значение, а только значение x[1]
    """

    return " ".join([i[0] for i in sort_dict.items()])


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order("" ))