from abc import ABC, abstractmethod

from ObserverPattern.Observers.IObserver import IObserver


class IObservable(ABC):
    @abstractmethod
    def add(self, observable: IObserver):
        raise NotImplementedError

    @abstractmethod
    def remove(self, observable: IObserver):
        raise NotImplementedError

    @abstractmethod
    def notify(self):
        raise NotImplementedError
    