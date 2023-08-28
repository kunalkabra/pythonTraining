from abc import ABC, abstractmethod

class Comp(ABC):
    @abstractmethod
    def do_something(self):
        pass

    @abstractmethod
    def do_nothing(self):
        pass
