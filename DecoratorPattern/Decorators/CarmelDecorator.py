from DecoratorPattern.Components.Beverage import Beverage
from DecoratorPattern.Decorators.AddonDecorator import AddonDecorator


class CarmelDecorator(AddonDecorator):
    def __init__(self, beverage: Beverage):
        self.__cost: float = 10
        self.__beverage = beverage

    def cost(self) -> float:
        return self.__beverage.cost() + self.__cost
