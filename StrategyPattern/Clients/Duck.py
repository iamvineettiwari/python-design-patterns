from StrategyPattern.Strategies import IFly
from StrategyPattern.Strategies.IDisplay import IDisplay
from StrategyPattern.Strategies.IQuack import IQuack


class Duck:
    def __init__(self, display: IDisplay, quack: IQuack, fly: IFly):
        self._display = display
        self._quack = quack
        self._fly = fly

    def quack(self):
        self._quack.quack()

    def fly(self):
        self._fly.fly()

    def display(self):
        self._display.display(data="I am a quack")

