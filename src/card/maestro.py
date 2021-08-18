from .plaincard import Card
from datetime import date

class Maestro(Card):

    def __init__(self, holdername: str) -> None:
        super().__init__(holdername)