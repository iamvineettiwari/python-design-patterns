from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first: str, last: str, pay: float, designation: str):
        self._first: str = first
        self._last: str = last
        self._pay: float = pay
        self._designation: str = designation

    def show_info(self):
        print('First Name: ' + self._first)
        print('Last Name: ' + self._last)
        print('Pay: ' + str(self._pay))
        print('Designation: ' + self._designation)

    @abstractmethod
    def do_work(self):
        raise NotImplementedError

