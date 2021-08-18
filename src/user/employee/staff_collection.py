from .staff_filter import StaffFilter
from src.user.employee import Staff
import random as rd

class StaffCollection:

    @staticmethod
    def rand_staff(staff: list[Staff]) -> Staff:
        if len(staff) <= 0:
            return None
        return rd.choice(staff)
    
    @staticmethod
    def filter(staff: list[Staff], staff_filter: StaffFilter) -> list[Staff]:
        return staff_filter.filter(staff)