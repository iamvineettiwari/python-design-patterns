from ObserverPattern.Observable.IObservable import IObservable
from ObserverPattern.Observers.IObserver import IObserver
from ObserverPattern.Data.IDataSourceReader import IDataSourceReader
from ObserverPattern.Data.IDataSourceWriter import IDataSourceWriter


class WeatherStation(IObservable, IDataSourceWriter, IDataSourceReader):

    def __init__(self):
        self.__temperature = 0
        self.__observables : list[IObserver] = list()

    def add(self, observable: IObserver):
        self.__observables.append(observable)

    def remove(self, observable: IObserver):
        self.__observables.remove(observable)

    def notify(self):
        for observable in self.__observables:
            observable.update()

    def get_data(self) -> float:
        return self.__temperature

    def write_data(self, data: float):
        self.__temperature = data
        self.notify()

