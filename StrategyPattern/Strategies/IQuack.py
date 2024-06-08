from abc import ABC, abstractmethod


class IQuack(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError
