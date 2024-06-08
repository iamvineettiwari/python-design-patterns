from FactoryMethodPattern.Product.Employee import Employee


class Programmer(Employee):
    def __init__(self, first: str, last: str, pay: float):
        super().__init__(first=first, last=last, pay=pay, designation='Programmer')

    def do_work(self):
        print("I am doing coding")
