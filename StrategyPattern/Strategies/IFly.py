from abc import ABC, abstractmethod


class IFLy(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError
