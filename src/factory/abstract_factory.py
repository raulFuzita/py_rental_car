from abc import ABC, abstractclassmethod

class AbstractFactory:

    @abstractclassmethod
    def make(self, param=None) -> None:
        raise NotImplementedError

    @abstractclassmethod
    def make_many(self, param=None) -> None:
        raise NotImplementedError