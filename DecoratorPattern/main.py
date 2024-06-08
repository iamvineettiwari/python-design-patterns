from DecoratorPattern.Components.Coffee import Coffee
from DecoratorPattern.Decorators.CarmelDecorator import CarmelDecorator
from DecoratorPattern.Decorators.CoconutMilkDecorator import CoconutMilkDecorator


def main():
    coffee = Coffee()

    print(f"Coffee is of cost : {coffee.cost()}")
    print(f"Coffee with carmel is of cost : {CarmelDecorator(beverage=coffee).cost()}")
    print(f"Coffee with double carmel is of cost : {CarmelDecorator(beverage=CarmelDecorator(beverage=coffee)).cost()}")
    print(f"Coffee with coconut milk is of cost : {CoconutMilkDecorator(beverage=coffee).cost()}")


if __name__ == '__main__':
    main()