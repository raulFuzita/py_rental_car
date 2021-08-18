from .staff import Staff

class Receptionist(Staff):

    def __init__(self, name: str='', salary: float=3000) -> None:
        super().__init__()
        self._name = name
        self._salary = salary

    def work(self) -> str:
        return 'Making phone calls'