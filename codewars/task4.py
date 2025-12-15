"""
Вы, вероятно, знакомы с системой «лайков» в Facebook и на других платформах.
Люди могут ставить «лайки» под постами в блогах, фотографиями и другими материалами.
Мы хотим создать текст, который будет отображаться рядом с таким материалом.

Реализуйте функцию, которая принимает массив с именами людей, которым нравится какой-либо товар.
Она должна возвращать текст для отображения, как показано в примерах:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Примечание: для 4 и более имён количество в "and 2 others" просто увеличивается.
"""


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))
