from abc import ABC, abstractclassmethod
from src.user.employee import Staff

class AbstractStaffFactory(ABC):

    @abstractclassmethod
    def make(self, name: str) -> Staff:
        raise NotImplementedError

    @abstractclassmethod
    def make_many(self, names: list[str]) -> list[Staff]:
        raise NotImplementedError
