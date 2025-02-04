# Dependency inversion principle

# BAD solution
"""
class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")


class App:
    def start(self):
        converter = FXConverter()
        converter.convert("EUR", "USD", 100)


if __name__ == '__main__':
    app = App()
    app.start()
"""

# GOOD solution
from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount):
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print("Converting currency using FX API.")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.2


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print("Converting currency using Alpha API.")
        print(f"{amount} {from_currency} = {amount * 1.15} {to_currency}")
        return amount * 1.15


class App:
    def __init__(self, converter):
        self.converter = converter

    def start(self, from_currency, to_currency, amount):
        self.converter.convert(from_currency, to_currency, amount)


if __name__ == '__main__':
    choice = input("Select converter: Alpha[A] or FX[F]: ")
    if choice == 'A':
        convertor = AlphaConverter()
    elif choice == 'F':
        convertor = FXConverter()
    else:
        convertor = AlphaConverter()
    app = App(convertor)
    from_currency = input("From currency: ")
    to_currency = input("To currency: ")
    amount = int(input("Amount: "))
    app.start(from_currency, to_currency, amount)