class Persoana:

    # respect incapsularea prin specificatorii de acces -> unul sau doua _ (underline)
    __nume = ""
    prenume = ""

    def __init__(self, prenume = "Prenume", nume = "Nume"):
        self.prenume = prenume
        self.__nume = nume
    
    def get_prenume(self):
        return self.prenume
    
    def prezentare(self):
        print(f"Salut, eu sunt {self.prenume} {self.__nume}")

class Student(Persoana):

    __nota = ""

    def __init__(self, prenume, nume, nota):
        Persoana().__init__(prenume, nume)     # apelez constructorul clasei parinte
        self.__nota = nota

    def prezentare(self):
        print(f"Salut, eu sunt {self.prenume} si am nota {self.__nota}.")

    def notare(self, nota):
        self.__nota = nota