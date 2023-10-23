import dearpygui.dearpygui as dpg


pretul_total = 0
order = []
kebab_dict = {"nume": "Kebab", "pret": 25, "ID": 1, "cantitate": 0}
cartofi_dict = {"nume": "Cartofi", "pret": 11, "ID": 2, "cantitate": 0}
suc_dict = {"nume": "Suc", "pret": 6, "ID": 3, "cantitate": 0}
meniu_dict = {"nume": "Meniu", "pret": 35, "ID": 4, "cantitate": 0}
taguri_cantitate = {"kebab": "uW7zErHsy4RMuwQr", "cartofi": "mzaluQCTuU5nxU+u",
                    "suc": "G6QzXDNP5KH0ZmCL", "meniu": "GyQS7LTrGPlgLbG4"}

# o functie callback care va fi de fiecare data
# executata cand se apasa pe butonul Add


def add_item(item_dict, item_tag):
    global pretul_total
    order.append(item_dict["nume"])
    item_dict["cantitate"] += 1
    dpg.set_value(taguri_cantitate[item_tag], item_dict["cantitate"])
    pretul_total += item_dict["pret"]


def button_callback(sender, app_data, select):
    global pretul_total
    if select == kebab_dict["ID"]:
        # Functia care adauga produsul in order si creste cantitatea
        add_item(kebab_dict, "kebab")

        # order.append(kebab_dict["nume"])
        # kebab_dict["cantitate"] += 1
        # dpg.set_value(taguri_cantitate["kebab"], kebab_dict["cantitate"])
        # pretul_total += kebab_dict["pret"]

    elif select == cartofi_dict["ID"]:
        add_item(cartofi_dict, "cartofi")

    elif select == suc_dict["ID"]:
        add_item(suc_dict, "suc")

    elif select == meniu_dict["ID"]:
        add_item(meniu_dict, "meniu")

    comanda_actuala = ", ".join(order)
    dpg.set_value("comanda_actuala", f"""Comanda actuala: 
                  {kebab_dict['cantitate']} x {kebab_dict['nume']}
    """)
    dpg.set_value("pretul_total", f"Pretul total: {pretul_total}")


def print_order():  # printam comanda
    print(order)


dpg.create_context()

# Creaza fereastra
with dpg.window(label="Custom Super Nice Window", tag="Primary Window"):
    dpg.add_text("Python Kebab", color=(243, 156, 22))  # culorile + text

# sectiune kebab

# Acestea pot fi modificate (scurtate). Puse intr-o functie separata. \/

    with dpg.collapsing_header(label=kebab_dict["nume"], default_open=False):
        dpg.add_text(
            f"{kebab_dict['nume']} : {kebab_dict['pret']} lei", color=(239, 219, 167))
        dpg.add_text(kebab_dict['cantitate'], tag=taguri_cantitate["kebab"])
        dpg.add_button(label="Add", callback=button_callback,
                       user_data=kebab_dict["ID"])

# sectiune cartofi

    with dpg.collapsing_header(label=cartofi_dict["nume"], default_open=False):
        dpg.add_text(
            f"{cartofi_dict['nume']} : {cartofi_dict['pret']} lei , ", color=((255, 255, 0)))
        dpg.add_text(cartofi_dict['cantitate'],
                     tag=taguri_cantitate["cartofi"])
        dpg.add_button(label="Add", callback=button_callback,
                       user_data=cartofi_dict["ID"])

# sectiune suc

    with dpg.collapsing_header(label=suc_dict["nume"], default_open=False):
        dpg.add_text(
            f"{suc_dict['nume']} : {suc_dict['pret']} lei , ", color=((0, 92, 184)))
        dpg.add_text(suc_dict['cantitate'], tag=taguri_cantitate["suc"])
        dpg.add_button(label="Add", callback=button_callback,
                       user_data=suc_dict["ID"])

# sectiune meniu

    with dpg.collapsing_header(label=meniu_dict["nume"], default_open=False):
        dpg.add_text(
            f"{meniu_dict['nume']} : {meniu_dict['pret']} lei ,", color=(184, 229, 250))
        dpg.add_text(cartofi_dict['cantitate'], tag=taguri_cantitate["meniu"])
        dpg.add_button(label="Add", callback=button_callback,
                       user_data=meniu_dict["ID"])

# Element text pentru afisarea listei cu produse

    dpg.add_text("Nu aveti nici un produs in cos.", tag="comanda_actuala")
    dpg.add_text(" ", tag="pretul_total")
    # printeaza comanda (da callback la print_order)
    dpg.add_button(label="Finalizeaza comanda", callback=print_order)


dpg.create_viewport(title='Custom Title', width=400, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
