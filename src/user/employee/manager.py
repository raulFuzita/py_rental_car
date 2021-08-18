from .staff import Staff

class Manager(Staff):

    def __init__(self, name: str='', salary: float=8000) -> None:
        super().__init__()
        self._name = name
        self._salary = salary

    @property
    def work(self) -> str:
        return 'Managing the store'