from .car_model import CarModel

class Luxury(CarModel):

    def __init__(self) -> None:
        self._model_name = self.__class__.__name__
        self._seats = 5
