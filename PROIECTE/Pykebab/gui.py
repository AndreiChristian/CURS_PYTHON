import dearpygui.dearpygui as dpg


pretul_total = 0
order = []
kebab_dict = {"nume": "Kebab", "pret": 25, "ID": 1, "cantitate": 0}
cartofi_dict = {"nume": "Cartofi", "pret": 11, "ID": 2, "cantitate": 0}
suc_dict = {"nume": "Suc", "pret": 6, "ID": 3, "cantitate": 0}
meniu_dict = {"nume": "Meniu", "pret": 35, "ID": 4, "cantitate": 0}


def button_callback(sender, app_data, select):

    global pretul_total

    if select == kebab_dict["ID"]:

        order.append(kebab_dict["nume"])

        pretul_total += kebab_dict["pret"]

    elif select == cartofi_dict["ID"]:

        order.append(cartofi_dict["nume"])

        pretul_total += cartofi_dict["pret"]

    elif select == suc_dict["ID"]:

        order.append(suc_dict["nume"])

        pretul_total += suc_dict["pret"]

    elif select == meniu_dict["ID"]:

        order.append(meniu_dict["nume"])

        pretul_total += meniu_dict["pret"]

    comanda_actuala = ", ".join(order)

    dpg.set_value("comanda_actuala", f"Comanda actuala: {comanda_actuala}")

    dpg.set_value("pretul_total", f"Pretul total: {pretul_total}")


def print_order():  # printam comanda

    print(order)


dpg.create_context()


with dpg.window(label="Custom Super Nice Window", tag="Primary Window"):  # Creaza fereastra

    dpg.add_text("Python Kebab", color=(243, 156, 22))  # culorile + text


# sectiune kebab

    with dpg.collapsing_header(label=kebab_dict["nume"], default_open=False):

        dpg.add_text(
            f"{kebab_dict['nume']} : {kebab_dict['pret']} lei", color=(239, 219, 167))

        # dpg.add_text(kebab_dict["nume"], color=(239,219,167))

        # dpg.add_text(kebab_dict["pret"], color=(239,219,167) )

        dpg.add_button(label="Add", callback=button_callback,
                       user_data=kebab_dict["ID"])


# sectiune cartofi

    with dpg.collapsing_header(label=cartofi_dict["nume"], default_open=False):

        dpg.add_text(
            f"{cartofi_dict['nume']} : {cartofi_dict['pret']} lei , {cartofi_dict['cantitate']}", color=((255, 255, 0)))

        dpg.add_button(label="Add", callback=button_callback,
                       user_data=cartofi_dict["ID"])


# sectiune suc

    with dpg.collapsing_header(label=suc_dict["nume"], default_open=False):

        dpg.add_text(
            f"{suc_dict['nume']} : {suc_dict['pret']} lei , {suc_dict['cantitate']}", color=((0, 92, 184)))

        dpg.add_button(label="Add", callback=button_callback,
                       user_data=suc_dict["ID"])


# sectiune meniu

    with dpg.collapsing_header(label=meniu_dict["nume"], default_open=False):

        dpg.add_text(
            f"{meniu_dict['nume']} : {meniu_dict['pret']} lei ,{cartofi_dict['cantitate']}", color=(184, 229, 250))

        dpg.add_button(label="Add", callback=button_callback,
                       user_data=meniu_dict["ID"])


# Element text pentru afisarea listei cu produse

    dpg.add_text("Nu aveti nici un produs in cos.", tag="comanda_actuala")

    dpg.add_text(" ", tag="pretul_total")

    # printeaza comanda (da callback la print_order)
    dpg.add_button(label="Finalizeaza comanda", callback=print_order)


dpg.create_viewport(title='Custom Title', width=600, height=200)

dpg.setup_dearpygui()

dpg.show_viewport()

dpg.set_primary_window("Primary Window", True)

dpg.start_dearpygui()
