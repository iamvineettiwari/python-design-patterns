from abc import ABC, abstractmethod


class IDataSourceReader(ABC):
    @abstractmethod
    def get_data(self) -> float:
        raise NotImplementedError
