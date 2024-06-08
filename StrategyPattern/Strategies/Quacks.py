from StrategyPattern.Strategies.IQuack import IQuack


class NoQuack(IQuack):

    def quack(self):
        print("I can not perform quacking")


class SimpleQuack(IQuack):

    def quack(self):
        print("Quack Quack")