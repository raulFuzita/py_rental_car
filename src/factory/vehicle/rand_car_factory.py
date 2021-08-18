from .car_factory import AbstractCarFactory
from src.vehicle.car import Car
from src.vehicle.bmw import BMW
from src.vehicle.ford import Ford
from src.vehicle.toyota import Toyota
from .model.rand_carmodel_factory import RandCarModelFactory
import random as rd

class RandCarFactory(AbstractCarFactory):

    def make(self) -> Car:
        car = self._createCar()
        factory = RandCarModelFactory()
        car.model = factory.make()
        return car

    def make_many(self, unit: int) -> list[Car]:
        cars = []
        for i in range(unit):
            cars.append(self.make())
        return cars

    def _createCar(self) -> Car:
        car_type = rd.randrange(3)
        if car_type == 0:
            return BMW()
        elif car_type == 1:
            return Ford()
        else:
            return Toyota()