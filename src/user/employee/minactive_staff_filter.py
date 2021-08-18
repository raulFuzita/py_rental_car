from .staff_filter import StaffFilter
from src.user.employee import Staff
import random as rd

class MinActiveStaffFilter(StaffFilter):
    
    def filter(self, staff: list[Staff]) -> list[Staff]:
        for s in staff:
            if s.active:
                return staff
        rd.choice(staff).active = True
        return staff