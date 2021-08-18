from datetime import date

class Builder:

    def __init__(self) -> None:
        self.expire_date = None
        self.card_number = None
        self.cvv = None

    def holder_name(self, holdername: str) -> None:
        raise NotImplementedError

    def expire_date(self, expiredate: date) -> None:
        raise NotImplementedError

    def card_number(self, cardnumber: int) -> None:
        raise NotImplementedError

    def cvv(self, number: int) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f'Builder(holder_name: "{self._holdername},  \
                expire_date: {self._expiredate}", \
                card_number: {self._cardnumber}, \
                cvv: {self._cvv})'