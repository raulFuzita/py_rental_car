from .card_factory import AbstractCardFactory
from src.card.mastercard import MasterCard
from src.util.random_date import *
import random as rd

class MasterCardFactory(AbstractCardFactory):

    def make(self, holdername: str) -> MasterCard:
        card = MasterCard(holdername)
        card.expire_date = rand_date(3)
        card.cvv = rd.randrange(999)
        return card