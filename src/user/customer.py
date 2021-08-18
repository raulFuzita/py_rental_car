from src.card import Card
from datetime import date

class Customer:
    
    def __init__(self, name: str, birthday: date, card: Card) -> None:
        self._name = name
        self._birthday = birthday
        self._card = card

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def birthday(self) -> date:
        return self._birthday

    @birthday.setter
    def birthday(self, birthday: date) -> None:
        self._birthday = birthday

    @property
    def card(self) -> Card:
        return self._card

    @card.setter
    def card(self, card: Card) -> None:
        self._card = card

    def __str__(self):
        return "{'name': '%s', 'birthday': '%s', 'card': '%s'}"\
            %(self._name, self._birthday, self._card)

    def __repr__(self):
        return f'Customer("{self._name}", "{self._birthday}", "{self._card}")'

    