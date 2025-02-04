from abc import ABC


class Drink(ABC):
    def get_volume(self):
        pass

    def is_addictive(self):
        pass

    def get_number_of_sugar_lumps(self):
        pass

    def get_taste(self):
        pass


class Coffee(Drink):
    def get_volume(self):
        return "150ml"

    def is_addictive(self):
        return True

    def get_number_of_sugar_lumps(self):
        return 0

    def get_taste(self):
        return "bitter"

    def __str__(self):
        return (f"Coffee with volume {self.get_volume()}, is additive, "
                f"with {self.get_number_of_sugar_lumps()} sugar lumps and "
                f"{self.get_taste()} taste.")


class Tea(Drink):
    def get_volume(self):
        return "250ml"

    def is_addictive(self):
        return False

    def get_number_of_sugar_lumps(self):
        return 2

    def get_taste(self):
        return "sweet"

    def __str__(self):
        return (f"Tea with volume {self.get_volume()}, is not additive, "
                f"with {self.get_number_of_sugar_lumps()} sugar lumps and "
                f"{self.get_taste()} taste.")


class DrinkPurchase(ABC):
    def buy(self, cost):
        pass


class CoffeePurchase(DrinkPurchase):

    def __init__(self):
        self._coffee = Coffee()

    def buy(self, cost):
        print(f"Buying a coffee for {cost}")
        return self._coffee

    def sell(self, volume):
        print(f"Selling a coffee of {volume} volume")
        return self._coffee


class TeaPurchase(DrinkPurchase):
    def __init__(self):
        self._tea = Tea()

    def buy(self, cost):
        print(f"Buying a tea for {cost}")
        return self._tea


def main():
    #coffee = Coffee()
    #tea = Tea()

    coffee_purchase = CoffeePurchase()
    print(coffee_purchase.buy(200))
    tea_purchase = TeaPurchase()
    print(tea_purchase.buy(150))

    # TODO: Upravte tak, aby bylo možné volit objem nápoje, počet cukrů a chuť.


if __name__ == '__main__':
    main()