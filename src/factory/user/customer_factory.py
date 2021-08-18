from . import AbstractUserFactory
from src.user import Customer
from src.factory.card import AbstractCardFactory, VisaCardFactory, \
MasterCardFactory, MaestroFactory
from src.util import rand_date
import random as rd

class CustomerFactory(AbstractUserFactory):

    def make(self, name) -> Customer:
        birthday = rand_date(-18, start=rd.randrange(75))
        factory = self._createCard()
        card = factory.make(name)
        return Customer(name, birthday, card)

    def make_many(self, names) -> list[Customer]:
        customers = []
        for name in names:
            customers.append(self.make(name))
        return customers

    def _createCard(self) -> AbstractCardFactory:
        card_type = rd.randrange(3)
        if card_type == 0:
            return MaestroFactory()
        elif card_type == 1:
            return MasterCardFactory()
        else:
            return VisaCardFactory()