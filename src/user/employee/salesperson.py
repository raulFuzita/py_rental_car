from .staff import Staff

class Salesperson(Staff):

    def __init__(self, name: str='', salary: float=5000) -> None:
        super().__init__()
        self._name = name
        self._salary = salary

    def work(self) -> str:
        return 'Selling cars to clients'