from FactoryMethodPattern.Product.Employee import Employee


class Accountant(Employee):
    def __init__(self, first: str, last: str, pay: float):
        super().__init__(first=first, last=last, pay=pay, designation='Accountant')

    def do_work(self):
        print("I am doing accounting related work")