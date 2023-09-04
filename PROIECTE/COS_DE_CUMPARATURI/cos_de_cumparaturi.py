cos = []


def adauga_produs():

    denumire = input("Ce produs vrei sa adaugi in cos?")

    pret = float(input("Pret:"))

    produs = {"denumire": denumire,

              "pret": pret,

              "cantitate": 1}

    cos.append(produs)


# adauga_produs()


def printeaza_cos():

    for element in cos:

        denumire = element["denumire"]
        pret = element["pret"]

        cantitate = element["cantitate"]

        print(
            f"Produsul ales este {denumire}, are pretul {pret} si cumparam {cantitate} bucati")

# printeaza_cos()


program_activ = True

while program_activ:

    optiunea_selectata = input("Selectati o optiune : ")

    if optiunea_selectata == "Q" or optiunea_selectata == "q":
        program_activ = False

    elif optiunea_selectata == "1":

        adauga_produs()

    elif optiunea_selectata == "2":

        printeaza_cos()
