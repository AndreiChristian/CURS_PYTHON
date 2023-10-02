class Kebab:
    def __init__(self):
        self.carne = []
        self.legume = []
        self.sosuri = []

    def adauga_carne(self, ingredient):
        self.carne.append(ingredient)

    def adauga_legume(self, ingredient):
        self.legume.append(ingredient)

    def adauga_sosuri(self, ingredient):
        self.sosuri.append(ingredient)

    def display(self):
        return f"Kebab with Carne: {' '.join(self.carne)}, Legume: {' '.join(self.legume)}, Sosuri: {' '.join(self.sosuri)}"


class KebabBuilder:

    def __init__(self):
        self.kebab = Kebab()

    def adauga_carne(self, meat):
        self.kebab.adauga_carne(meat)
        return self

    def adauga_legume(self, legume):
        self.kebab.adauga_legume(legume)
        return self

    def adauga_sos(self, sos):
        self.kebab.adauga_sosuri(sos)
        return self

    def finalizeaza(self):
        return self.kebab


kebabBuiler = KebabBuilder()
kebab = kebabBuiler.adauga_carne("vita").adauga_sos(
    "maioneza").adauga_legume("rosii").finalizeaza()
print(kebab.display())
