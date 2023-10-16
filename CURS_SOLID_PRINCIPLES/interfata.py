from abc import ABC, abstractmethod


class Forma(ABC):

    @abstractmethod
    def perimetru(self):

        pass

    @abstractmethod
    def arie(self):

        pass


class Patrat(Forma):

    def __init__(self, latura):

        self.latura = latura

    def perimetru(self):

        return self.latura * 4  # 10 * 4

    def arie(self):

        return self.latura ** 2  # 10 * 10


patrat_1 = Patrat(10)

print(patrat_1.perimetru())

# poate fi super confuz sa primesti o valoare cu totul neaspteptata

print(patrat_1.arie())
