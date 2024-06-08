from StrategyPattern.Strategies.IDisplay import IDisplay


class AnalogDisplay(IDisplay):
    def display(self, data: str):
        print("Enabling analog display")
        print(data)


class DigitalDisplay(IDisplay):
    def display(self, data: str):
        print("Enabling digital display")
        print(data)

