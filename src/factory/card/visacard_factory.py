from .card_factory import AbstractCardFactory
from src.card.visacard import VisaCard
from src.util.random_date import *
import random as rd

class VisaCardFactory(AbstractCardFactory):

    def make(self, holdername: str) -> VisaCard:
        card = VisaCard(holdername)
        card.expire_date = rand_date(3)
        card.cvv = rd.randrange(999)
        return card
