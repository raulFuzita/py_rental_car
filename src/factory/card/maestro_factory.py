from .card_factory import AbstractCardFactory
from src.card.maestro import Maestro
from src.util.random_date import *
import random as rd

class MaestroFactory(AbstractCardFactory):

    def make(self, holdername: str) -> Maestro:
        card = Maestro(holdername)
        card.expire_date = rand_date(3)
        card.cvv = rd.randrange(999)
        return card