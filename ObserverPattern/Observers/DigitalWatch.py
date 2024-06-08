from ObserverPattern.Data.IDataSourceReader import IDataSourceReader
from ObserverPattern.Observers.IObserver import IObserver


class DigitalWatch(IObserver):
    def __init__(self, weather_station: IDataSourceReader):
        self.__weather_station = weather_station

    def update(self):
        print("Displaying on watch : ", self.__weather_station.get_data())
        
