from .plaincard import Card
from datetime import date

class MasterCard(Card):

    def __init__(self, holdername: str) -> None:
        super().__init__(holdername)

