from abc import ABC, abstractclassmethod
from itertools import count

class Staff(ABC):

    _id_staff = count(1)

    def __init__(self) -> None:
        self._id = next(self._id_staff)
        self._active = False

    @property
    def name(self) -> None:
        return self._name

    @name.setter
    def name(self, name: str) -> str:
        self._name = name

    @property
    def salary(self) -> None:
        return self._salary

    @salary.setter
    def salary(self, salary: float) -> float:
        self._salary = salary

    @property
    def active(self) -> None:
        return self._active

    @active.setter
    def active(self, active: bool) -> bool:
        self._active = active

    @property
    @abstractclassmethod
    def work(self) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        staffname = self.__class__.__name__
        return "{'role': '%s', 'id': %s, 'name': '%s', 'salary': %s, 'active': %s}"\
                %(staffname, self._id, self._name, self._salary, self._active)

    def __repr__(self) -> str:
        staffname = self.__class__.__name__
        return "%s(%s, %s, %s, %s)"\
            %(staffname, self._id, self._name, self._salary, self._active)