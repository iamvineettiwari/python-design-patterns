from StrategyPattern.Strategies.IFly import IFLy


class SimpleFly(IFLy):
    def fly(self):
        print("Flying")


class NoFly(IFLy):
    def fly(self):
        print("Can not fly")