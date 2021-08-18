from src.user.employee import Salesperson
from src.vehicle import Car
from src.user import Customer
from src.rent import Record
import random as rd

class RentalCarFacade:

    def __init__(self, salespersons: list[Salesperson], cars: list[Car]) -> None:
        self._salespersons = salespersons
        self._cars = cars

    def rent_car(self, customer: Customer) -> Record:
        staff = rd.choice(self._salespersons)
        car = rd.choice(self._cars)
        self._cars.remove(car)
        return Record(customer, staff, car)