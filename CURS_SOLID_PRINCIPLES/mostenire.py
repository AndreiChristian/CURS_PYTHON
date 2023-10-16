# clasa de baza
class Animal:
    def fa_zgomot(self):
        print("Sunet de animal")

# clasa care mosteneste explicit ( suprascrie/override metoda
# deja existenta dar
# ceea ce face de fapt este
# foloseste clasa deja existenta a parintelui)

class Caine(Animal):
    def fa_zgomot(self):
        return super().fa_zgomot()

# clasa care mosteneste de la parinte dar suprascire/override
# metoda si are o logica diferita

class Pisica(Animal):
    def fa_zgomot(self):
        print("Miau")

# clasa care mosteneste implicit de la parinte


class Peste(Animal):

    # o metoda care nu are nicio legatura,
    # dar care exista doar pt a nu primi eroare
    def inoata(self):
        print("Inot si sunt super fericit")


caine = Caine()
caine.fa_zgomot()

pisica = Pisica()
pisica.fa_zgomot()

peste = Peste()
peste.fa_zgomot()
