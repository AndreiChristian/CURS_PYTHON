class Bautura:
    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret


class Cola(Bautura):
    def __init__(self):
        super().__init__("Cola", 10)


class Fanta(Bautura):
    def __init__(self):
        super().__init__("Fanta", 9)


class Sprite(Bautura):
    def __init__(self):
        super().__init__("Sprite", 11)
