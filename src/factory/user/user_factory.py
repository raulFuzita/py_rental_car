from src.user.customer import Customer

class AbstractUserFactory:

    def make(self, name) -> Customer:
        raise NotImplementedError

    def make_many(self, names) -> list[Customer]:
        raise NotImplementedError