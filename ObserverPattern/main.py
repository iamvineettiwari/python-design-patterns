from ObserverPattern.Observable.WeatherStation import WeatherStation
from ObserverPattern.Observers.Mobile import Mobile
from ObserverPattern.Observers.DigitalWatch import DigitalWatch
import time


def main():
    weather_station = WeatherStation()

    digital_watch = DigitalWatch(weather_station=weather_station)
    mobile = Mobile(weather_station=weather_station)

    weather_station.add(digital_watch)
    weather_station.add(mobile)

    for i in range(10):
        weather_station.write_data(round((i + 1) * 12.56, 2))
        time.sleep(1)
        print()

        if i == 7:
            weather_station.remove(mobile)


if __name__ == '__main__':
    main()
