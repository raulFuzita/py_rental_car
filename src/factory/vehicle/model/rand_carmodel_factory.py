from .carmodel_factory import AbstractCardModelFactory
from src.vehicle.model.car_model import CarModel
from src.vehicle.model.family import Family
from src.vehicle.model.luxury import Luxury
from src.vehicle.model.sport import Sport
import random as rd

class RandCarModelFactory(AbstractCardModelFactory):

    def make(self) -> CarModel:
        return self._rand_model()

    def _rand_model(self) -> CarModel:
        model_type = rd.randrange(3)
        if model_type == 0:
            return Sport()
        elif model_type == 1:
            return Luxury()
        else:
            return Family()
