from StrategyPattern.Clients import WildDuck, CityDuck, RubberDuck
from StrategyPattern.Strategies.Quacks import SimpleQuack, NoQuack
from StrategyPattern.Strategies.Flies import SimpleFly, NoFly
from StrategyPattern.Strategies.Displays import AnalogDisplay, DigitalDisplay


def main():
    sq = SimpleQuack()
    nq = NoQuack()

    sf = SimpleFly()
    nf = NoFly()

    dd = DigitalDisplay()
    ad = AnalogDisplay()

    wild_duck = WildDuck(quack=sq, fly=sf, display=ad)
    wild_duck.display()
    wild_duck.quack()
    wild_duck.fly()

    print("\n\n")

    city_duck = CityDuck(quack=sq, fly=sf, display=ad)
    city_duck.display()
    city_duck.quack()
    city_duck.fly()

    print("\n\n")

    rubber_duck = RubberDuck(quack=nq, fly=nf, display=dd)
    rubber_duck.display()
    rubber_duck.quack()
    rubber_duck.fly()

    print("\n\n")


if __name__ == '__main__':
    main()