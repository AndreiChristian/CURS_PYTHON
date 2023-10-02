class Animal():

    def __init__(self, greutate=20, varsta=90, nume="leopard"):
        self.__greutate = greutate
        self._varsta = varsta
        self.nume = nume

    def o_functie(self):
        print("Hello")


pisica = Animal()
caine = Animal(greutate=30,nume="pisica")

print(pisica._varsta)
pisica.o_functie()



print(pisica._Animal__greutate)