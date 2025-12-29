"""Модель данных в Python"""

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


# namedtuple - конструктор для простого класса, создали класс с одной картой (число и масть)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")  # карты
    suits = 'spades diamonds clubs hearts'.split()  # масти

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]  # карта со значением и мастью

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)
print(len(beer_card.rank))

card = FrenchDeck()
print(choice(card))  # выбираем случайную карту
