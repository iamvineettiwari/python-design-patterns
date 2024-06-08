from FactoryMethodPattern.Creator.Department import Department
from FactoryMethodPattern.Product.Accountant import Accountant
from FactoryMethodPattern.Product.Employee import Employee


class AccountingDepartment(Department):
    def __init__(self):
        self._da: float = 1539.90
        self._bonus: float = 2_00_000
        self._gratuity: float = 1_000_000
        self._department: str = 'Accounting'

    def create_employee(self, first: str, last: str, base: float) -> Employee:
        final_pay = base + self._da + self._bonus + self._gratuity
        return Accountant(first=first, last=last, pay=final_pay)
