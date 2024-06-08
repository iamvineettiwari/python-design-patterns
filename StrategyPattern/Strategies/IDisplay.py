from abc import ABC, abstractmethod


class IDisplay(ABC):
    @abstractmethod
    def display(self, data: str):
        raise NotImplementedError
