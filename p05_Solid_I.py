# Dependency inversion principle
# Bad Solution
"""

class FXConvertor:
    def convert(self, from_currency, to_currency, amount):
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")


class App:
    def start(self):
        convertor = FXConvertor()
        convertor.convert("Eur", "USD", 100)


if __name__ == "__main__":
    app = App()
    app.start()
"""

# Good solution

from abc import ABC

class CurrencyConverter(ABC):
    def convert(self,from_currency, to_currency, amount):
        pass


class FXConverter(CurrencyConverter):
    def convert(self,from_currency, to_currency, amount):
        print("Using FXConvertor")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.2

class AlphaConverter(CurrencyConverter):
    def convert(self,from_currency, to_currency, amount):
        print("Using AlphaConvertor")
        print(f"{amount} {from_currency} = {amount * 1.5} {to_currency}")
        return amount * 1.5

class App:
    def __init__(self, converter):
        self.converter = converter

    def start(self, from_currency, to_currency, amount):
        self.converter.convert(from_currency, to_currency, amount)

if __name__ == "__main__":
    choice = input("Select converter: Alpha[A] or FX[F]: ")
    if choice == "A":
        convertor = AlphaConverter()
    elif choice == "F":
        convertor = FXConverter()
    else:
        convertor = AlphaConverter()
    app = App(convertor)
    from_curency = input("From currency: ")
    to_currency = input("To currency: ")
    amount = int(input("Amount: "))
    app.start(from_curency, to_currency, amount)