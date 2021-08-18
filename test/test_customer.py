import sys

sys.path.append('..')

from src.user import Customer
from datetime import date

if __name__ == "__main__":
    c = Customer('John', date.today(), '0000-0000-0000-0000')

    print(c)
    print(repr(c))