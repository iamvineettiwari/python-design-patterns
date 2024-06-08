from StrategyPattern.Clients.Duck import Duck
from StrategyPattern.Strategies import IFly
from StrategyPattern.Strategies.IDisplay import IDisplay
from StrategyPattern.Strategies.IQuack import IQuack


class CityDuck(Duck):
    def __init__(self, display: IDisplay, quack: IQuack, fly: IFly):
        super().__init__(display, quack, fly)

    def display(self):
        self._display.display("I am a city duck")