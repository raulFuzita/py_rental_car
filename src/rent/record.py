from src.user import Customer
from src.user.employee import Staff
from src.vehicle import Car
from datetime import datetime

class Record:
    
    def __init__(self, customer: Customer, staff: Staff, car: Car) -> None:
        self._customer = customer
        self._staff = staff
        self._car = car
        self._timestamp = datetime.now().time()

    @property
    def customer(self) -> Customer:
        return self._customer

    @property
    def staff(self) -> Staff:
        return self._staff

    @property
    def car(self) -> Car:
        return self._car

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def __str__(self) -> str:
        return "{'customer': '%s', 'staff': '%s', 'car': '%s', 'timestamp': '%s'}"\
                %(self._customer, self._staff, self._car, self._timestamp)

    def __repr__(self) -> str:
        return "Record('%s', '%s', '%s', %s)"\
                %(self._customer, self._staff, self._car, self._timestamp)