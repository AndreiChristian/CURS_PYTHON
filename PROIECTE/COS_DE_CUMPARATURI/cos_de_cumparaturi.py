cos = []


def selecteaza_prodsul_dupa_nume(denumire):
    for produs in cos:
        if produs['denumire'] == denumire:
            return produs


def adauga_in_cos():
    denumire = input("Introduceti denumirea produsului : ")
    cantitate = int(input("Introduceti canitatea : "))
    pret = int(input("Introduceti pretul produsului : "))
    produs_nou = {
        "denumire": denumire,
        "pret": pret,
        "cantitate": cantitate
    }
    cos.append(produs_nou)


def printeaza_cosul():
    for produs in cos:
        denumire = produs['denumire']
        pret = produs['pret']
        cantitate = produs['cantitate']
        print(f"{denumire}, {pret} lei, {cantitate} bucati in cos.")


def elimintati_un_produs_din_cos(denumire):
    produsul_de_eliminat = selecteaza_prodsul_dupa_nume(denumire)
    if produsul_de_eliminat:
        cos.remove(produsul_de_eliminat)
        print("Prdosul a fost eliminat cu succes!")
    else:
        print("Produsul cautat nu a fost gasit !")


programul_este_activ = True
while programul_este_activ:
    print()
    print("1. Adaugati un produs nou.")
    print("2. Printati cosul.")
    print("3. Eliminati un produs din cos.")
    print()
    print("Apasati q/Q pentru a iesi")
    print()
    print("Selectati o optiune")
    optiunea_selectata = input("Optiunea dumneavoastra : ")
    print()
    if optiunea_selectata == "q" or optiunea_selectata == "Q":
        programul_este_activ = False
        print("")
        print("La revedere!")
    elif optiunea_selectata == "1":
        adauga_in_cos()
    elif optiunea_selectata == "2":
        printeaza_cosul()
    elif optiunea_selectata == "3":
        produsul_de_eliminat = input("Ce produs doriti sa eliminati ?")
        elimintati_un_produs_din_cos(produsul_de_eliminat)
