import random

lista_intrebari = [
    {'titlu': "Care este cel mai înalt munte din lume?", 'variante': [
        "Mount Everest", "K2", "Annapurna", "Mount Kilimanjaro"], 'raspuns_corect': "1"},
    {'titlu': "Cât de rapid poate să alerge un ghepard?", 'variante': [
        "60 km/h", "120 km/h", "90 km/h", "45 km/h"], 'raspuns_corect': "2"},
    {'titlu': "Cine a fost primul om care a ajuns pe Lună?", 'variante': [
        "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"], 'raspuns_corect': "1"},
    {'titlu': "Care este cel mai mare ocean de pe Pământ?", 'variante': [
        "Oceanul Atlantic", "Oceanul Pacific", "Oceanul Indian", "Oceanul Arctic"], 'raspuns_corect': "2"},
    {'titlu': "Ce planetă este cunoscută ca „Planeta Roșie”?", 'variante': [
        "Marte", "Venus", "Jupiter", "Saturn"], 'raspuns_corect': "1"},
    {'titlu': "Care este cea mai veninoasă meduză din lume?", 'variante': [
        "Meduza Luminată", "Meduza Box", "Meduza Luna", "Meduza Comună"], 'raspuns_corect': "2"},
    {'titlu': "În ce țară se găsește desertul Sahara?", 'variante': [
        "Egipt", "Maroc", "Libia", "Toate cele de mai sus"], 'raspuns_corect': "4"},
    {'titlu': "Care este cel mai lung fluviu din lume?", 'variante': [
        "Nilul", "Amazon", "Yangtze", "Mississippi"], 'raspuns_corect': "2"},
    {'titlu': "Câte inimi are o caracatiță?", 'variante': [
        "1", "2", "3", "4"], 'raspuns_corect': "3"},
    {'titlu': "Ce țară este cunoscută ca „Țara Soarelui Răsare”?", 'variante': [
        "China", "Japonia", "Coreea de Sud", "Vietnam"], 'raspuns_corect': "2"},
    {'titlu': "Ce animale sunt renumite pentru migrația lor anuală în Serengeti?", 'variante': [
        "Elefanți", "Gnus", "Zebre", "Toate cele de mai sus"], 'raspuns_corect': "4"},
]

intrebarea_1 = {'titlu': "Care este cel mai înalt munte din lume?", 'variante': [
    "Mount Everest", "K2", "Annapurna", "Mount Kilimanjaro"], 'raspuns_corect': "1"}

# scor = 0
# print(intrebarea_1["titlu"])
# for varianta in intrebarea_1["variante"]:
#     print(varianta)
# varianta_aleasa = input("Alegeti o varianta (1-4)")
# if varianta_aleasa == intrebarea_1["raspuns_corect"]:
#     scor += 1
#     print("Ati ales corect")

# print(scor)

random.shuffle(lista_intrebari)

scor = 0
for intrebare in lista_intrebari:
    print(intrebare["titlu"])
    for varianta in intrebare["variante"]:
        print(varianta)
    varianta_aleasa = input("Alegeti o varianta")
    if varianta_aleasa == intrebare["raspuns_corect"]:
        scor += 1
        print('Ati ales corect')

print(f"Scor final : {scor}/{len(lista_intrebari)}")
