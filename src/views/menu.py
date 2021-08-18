from src.vehicle import Car
from src.user.employee import Staff
from src.user.customer import Customer
from src.rent import Record
import sys

class Menu:

    def cars(self, cars: list[Car]):
        self._cars = cars
        return self

    def staff(self, staff: list[Staff]):
        self._staff = staff
        return self

    def customers(self, customers: list[Customer]):
        self._customers = customers
        return self

    def records(self, records: list[Record]):
        self._records = records
        return self

    def show_menu(self):
        op = 0
        while op != '7':
            print('============== Menu ==============')
            print('| (1) List all staff             |')
            print('| (2) List all customers         |')
            print('| (3) List all cars              |')
            print('| (4) List all records           |')
            print('| (5) List staff by categories   |')
            print('| (6) List cars by various types |')
            print('| (7) Exit                       |')
            print('----------------------------------')

            op = input('Enter a valid option: ')
            if op == '1': # List all staff
                print([s for s in self._staff])
            elif op == '2': # List all customers
                print([c for c in self._customers])
            elif op == '3': # List all cars
                print([c for c in self._cars])
            elif op == '4': # List all records
                print([r for r in self._records])
            elif op == '5': # List staff by categories
                sc = input('Enter staff category: ').lower()
                print([s for s in self._staff if s.__class__.__name__.lower() == sc])
            elif op == '6': # List cars by various types
                ct = input('Enter car type: ').lower()
                print([c for c in self._cars if c.__class__.__name__.lower() == ct])
            elif op == '7': # Exit
                print('Exit the menu')
            else:
                print("Option doesn't exist. Try again.")
            print()


        