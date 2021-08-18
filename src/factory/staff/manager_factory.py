from .staff_factory import AbstractStaffFactory
from src.user.employee import Manager

class ManagerFactory(AbstractStaffFactory):

    def make(self, name: str) -> Manager:
        return Manager(name)

    def make_many(self, names: list[str]) -> list[Manager]:
        managers = []
        for name in names:
            managers.append(Manager(name))
        return managers