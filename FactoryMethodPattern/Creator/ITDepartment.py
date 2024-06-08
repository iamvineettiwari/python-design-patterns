from FactoryMethodPattern.Creator.Department import Department
from FactoryMethodPattern.Product.Employee import Employee
from FactoryMethodPattern.Product.Programmer import Programmer


class ITDepartment(Department):
    def __init__(self):
        self._da: float = 1539.90
        self._bonus: float = 2_00_000
        self._department: str = 'IT'

    def create_employee(self, first: str, last: str, base: float) -> Employee:
        final_pay = base + self._da + self._bonus
        return Programmer(first=first, last=last, pay=final_pay)
