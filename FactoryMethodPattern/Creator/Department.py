from abc import ABC, abstractmethod

from FactoryMethodPattern.Product.Employee import Employee


class Department(ABC):
    @abstractmethod
    def create_employee(self, first: str, last: str, base: float) -> Employee:
        raise NotImplementedError
