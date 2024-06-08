from abc import ABC, abstractmethod


class IDataSourceWriter(ABC):
    @abstractmethod
    def write_data(self, data: float):
        raise NotImplementedError
