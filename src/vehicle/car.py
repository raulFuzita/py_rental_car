from .model.car_model import CarModel
from itertools import count

class Car:
    
    _uniq_carplate = count(1)

    def __init__(self) -> None:
        self._carplate = next(self._uniq_carplate)
        self._brand = self.__class__.__name__
        self._model = None
    
    @property
    def carplate(self) -> int:
        return self._carplate

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> CarModel:
        return self._model

    @model.setter
    def model(self, model: CarModel) -> None:
        self._model = model

    def __str__(self) -> str:
        return ("{'brand': %s, 'carplate': %s, 'model': %s}")\
                %(self._brand, self._carplate, self._model)

    def __repr__(self) -> str:
        return ('Car("%s", %s, %s)')\
                %(self._brand, self._carplate, self._model)