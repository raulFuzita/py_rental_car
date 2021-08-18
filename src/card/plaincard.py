from .builder import Builder
from datetime import date
from itertools import count

class Card(Builder):

    _uniq_cardnumber = count(1)

    def __init__(self, holdername: str) -> None:
        self._holdername = holdername
        self.expire_date = date.today()
        self.cvv = 0
        self.card_number = next(self._uniq_cardnumber)

    @property
    def holder_name(self) -> str:
        return self._holdername

    @holder_name.setter
    def holder_name(self, holdername: str) -> None:
        self._holdername = holdername

    @property
    def expire_date(self) -> date:
        return self._expiredate

    @expire_date.setter
    def expire_date(self, expiredate: date) -> None:
        self._expiredate = expiredate

    @property
    def card_number(self) -> int:
        return self._cardnumber

    @card_number.setter
    def card_number(self, cardnumber: int) -> None:
        self._cardnumber = cardnumber

    @property
    def cvv(self) -> int:
        return self._cvv

    @cvv.setter
    def cvv(self, number: int) -> None:
        self._cvv = number

    def __str__(self) -> str:
        return ("{'holder_name': '%s', 'expire_date': '%s', "
                "'card_number': %s, 'cvv': %s}"
                %(self._holdername, self._expiredate, 
                self._cardnumber, self._cvv))

    def __repr__(self) -> str:
        return ('Card("%s", "%s", %s, %s)') \
                %(self._holdername, self._expiredate, 
                self._cardnumber, self._cvv)