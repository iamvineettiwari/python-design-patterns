from abc import abstractmethod

from DecoratorPattern.Components.Beverage import Beverage


class AddonDecorator(Beverage):

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError
