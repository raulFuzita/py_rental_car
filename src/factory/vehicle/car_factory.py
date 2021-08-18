from src.vehicle.car import Car

class AbstractCarFactory:

    def make(self) -> Car:
        raise NotImplementedError

    def make_many(self) -> list[Car]:
        raise NotImplementedError
