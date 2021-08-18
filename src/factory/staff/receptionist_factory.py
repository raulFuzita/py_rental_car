from .staff_factory import AbstractStaffFactory
from src.user.employee import Receptionist

class ReceptionistFactory(AbstractStaffFactory):

    def make(self, name: str) -> Receptionist:
        return Receptionist(name)

    def make_many(self, names: list[str]) -> list[Receptionist]:
        managers = []
        for name in names:
            managers.append(self.make(name))
        return managers