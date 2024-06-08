from DecoratorPattern.Components.Beverage import Beverage
from DecoratorPattern.Decorators.AddonDecorator import AddonDecorator


class CoconutMilkDecorator(AddonDecorator):
    def __init__(self, beverage: Beverage):
        self.__cost: float = 25.58
        self.__beverage = beverage

    def cost(self) -> float:
        return self.__beverage.cost() + self.__cost
