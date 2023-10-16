# cand am vrea sa folosim inheritence
from abc import ABC, abstractmethod


class Persoana:
    def __init__(self, nume, prenume) -> None:
        self.nume = nume
        self.prenume = prenume

    def saluta(self):
        return f"Buna ziua! Numele meu este {self.nume} {self.prenume}"


class Angajat(Persoana):
    def __init__(self, nume, prenume, salariu) -> None:
        super().__init__(nume, prenume)
        self.salariu = salariu

    def calculeaza_taxe(self):
        return self.salariu * 0.46


class Senior_Developer(Angajat):

    def __init__(self, nume, prenume, salariu, ani_de_experienta) -> None:
        super().__init__(nume, prenume, salariu)
        self.ani_de_experienta = ani_de_experienta

    def design_complex_stuff(self):
        return f"Am {self.ani_de_experienta} asa ca stiu ca trb sa facem programul asa"


marcel = Angajat("Marcel", "Popescu", 4000)
print(marcel.saluta())
print(marcel.calculeaza_taxe())

george = Senior_Developer("George", "Ionescu", 10000, 10)
print(george.saluta())
print(george.calculeaza_taxe())
print(george.design_complex_stuff())

# cand am vrea sa folosim interfete
# CRUD -> Create, Read, Update, Delete


class CrudRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class Bicicleta_CRUD(CrudRepository):

    def create(self):
        pass

    def read(self, id):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class Anajagati_CRUD(CrudRepository):

    def create(self):
        pass


bicicleta_CRUD = Bicicleta_CRUD()

angajati_CURD = Anajagati_CRUD()
