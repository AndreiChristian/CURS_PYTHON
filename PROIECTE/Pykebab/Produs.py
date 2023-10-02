class Produs:
    def __init__(self, denumire, pret):
        self.denumire = denumire
        self.pret = pret

    def printeaza_info(self):
        print(f"{self.denumire} - {self.pret} lei")
