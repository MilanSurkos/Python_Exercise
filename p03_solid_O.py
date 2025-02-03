# Open/close principle
from abc import ABC, abstractmethod


class Operations(ABC):
    @abstractmethod
    def operation(list_):
        pass


class Mean(Operations):
    def __init__(self):
        pass

    @abstractmethod
    def operation(list_):
        return sum(list_) / len(list_)


class Min(Operations):
    def __init__(self):
        pass

    @abstractmethod
    def operation(list_):
        return min(list_)


class Max(Operations):
    def __init__(self):
        pass

    @abstractmethod
    def operation(list_):
        return max(list_)


class Main:
    def get_operations(self, list__):
        #print(f"Mean is {Mean.operation(list_=list__)}")
        for concrete_operation in Operations.__subclasses__():
            print(concrete_operation.operation(list_=list__))


if __name__ == '__main__':
    m = Main()
    m.get_operations(list__=[1, 2, 3, 4, 5, 6, 7])