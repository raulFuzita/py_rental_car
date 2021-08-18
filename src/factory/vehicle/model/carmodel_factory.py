from src.vehicle.model.car_model import CarModel

class AbstractCardModelFactory:

    def make() -> CarModel:
        raise NotImplementedError