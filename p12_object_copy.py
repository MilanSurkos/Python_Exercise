from copy import copy


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


human1 = Human("Petr")
print(human1)

human2 = human1
print(human2)

human1.name = "Martin"
print(f"human1: {human1}")
print(f"human2: {human2}")

human3 = copy(human1)
print(f"human1: {human1}, human2: {human2}, human3: {human3}")
human1.name = "Dušan"
print(f"human1: {human1}, human2: {human2}, human3: {human3}")

#