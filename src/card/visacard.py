from .plaincard import Card
from datetime import date

class VisaCard(Card):

    def __init__(self, holdername: str) -> None:
        super().__init__(holdername)
