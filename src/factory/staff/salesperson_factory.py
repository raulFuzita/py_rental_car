from .staff_factory import AbstractStaffFactory
from src.user.employee import Salesperson

class SalespersonFactory(AbstractStaffFactory):

    def make(self, name: str) -> Salesperson:
        return Salesperson(name)

    def make_many(self, names: list[str]) -> list[Salesperson]:
        managers = []
        for name in names:
            managers.append(self.make(name))
        return managers