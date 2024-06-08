from DecoratorPattern.Components.Beverage import Beverage


class Coffee(Beverage):

    def cost(self) -> float:
        return 15.0

    