from .staff_factory import AbstractStaffFactory
from .manager_factory import ManagerFactory
from .salesperson_factory import SalespersonFactory
from .receptionist_factory import ReceptionistFactory
from src.user.employee import Staff
import random as rd

class RandStaffFactory(AbstractStaffFactory):

    def make(self, name: str) -> Staff:
        factory = self._createFactory()
        staff = factory.make(name)
        staff.active = self._randActiveStatus()
        return staff

    def make_many(self, names: list[str]) -> list[Staff]:
        managers = []
        for name in names:
            managers.append(self.make(name))
        return managers

    def _createFactory(self) -> Staff:
        staff_type = rd.randrange(3)
        if staff_type == 0:
            return ManagerFactory()
        elif staff_type == 1:
            return SalespersonFactory()
        else:
            return ReceptionistFactory()

    def _randActiveStatus(self) -> bool:
        status = rd.randrange(2)
        if status == 0:
            return True
        else:
            return False
