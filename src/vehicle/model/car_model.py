
class CarModel:

    def __init__(self) -> None:
        self._model_name = self.__class__.__name__
        self._seats = 0

    def get_model(self):
        return self._model_name

    def get_seats(self):
        return self._seats

    def __str__(self) -> str:
        return ("{'model_name': %s, 'seats': %s}")\
                %(self._model_name, self._seats)

    def __repr__(self) -> str:
        modelname = self.__class__.__name__
        return "{modelname}({self._model_name}, {self._seats})"