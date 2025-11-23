import random

class Kamion:
    def __init__(self, kamionId, rendszam, teherbiras, fogyasztas, helyzet, kuldetes_idotartam):
        self.kamionId = int(kamionId)
        self.rendszam = rendszam
        self.teherbiras = int(teherbiras)
        self.fogyasztas = float(fogyasztas)
        self.helyzet = helyzet
        self.kuldetes_idotartam = int(kuldetes_idotartam)

kamionok = []
with open("kamionok.txt", "r", encoding="utf-8") as file:
    next(file) 
    for sor in file:
        parts = sor.strip().split(";")
        kamion = Kamion(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
        kamionok.append(kamion)



# függvények


def kamion_adatok_lekeres(kamionId):
    for kamion in kamionok:
        if kamion.kamionId == kamionId:
            return kamion
    return None

def rendszam_lekeres(kamionId):
    for kamion in kamionok:
        if kamion.kamionId == kamionId:
            return kamion.rendszam
    return None

def megrendeles():
    tomeg = int(input("Adja meg a szállítandó tömeget tonnában: "))
    szukseges_kamionok = []
    for kamion in kamionok:
        if kamion.helyzet == "telephelyen":
            szukseges_kamionok.append(kamion)
            if sum(i.teherbiras for i in szukseges_kamionok) >= tomeg:
                break
    if sum(i.teherbiras for i in szukseges_kamionok) >= tomeg:
        return szukseges_kamionok
    else:
        kuldetesen_levok = [i for i in kamionok if i.helyzet != "telephelyen"]
        leghamarabb_szabadulo = min(kuldetesen_levok, key=lambda x: x.kuldetes_idotartam)
        print(f"Nincs elegendő kapacitás. A leghamarabb szabaduló kamion ID-ja: {leghamarabb_szabadulo.kamionId}, mely {leghamarabb_szabadulo.kuldetes_idotartam} nap múlva lesz elérhető.")
        return None

def fogyasztas_lekeres(kamionId):
    for kamion in kamionok:
        if kamion.kamionId == kamionId:
            return kamion.fogyasztas
    return None

def rendelkezesre_allo_kamion_flotta():
    telephelyen_levok = [i for i in kamionok if i.helyzet == "telephelyen"]
    kuldetesen_levok = [i for i in kamionok if i.helyzet != "telephelyen"]
    return telephelyen_levok, kuldetesen_levok

def idomulas(napok):
    for i in kamionok:
        if i.helyzet == "kuldetesen":
            i.kuldetes_idotartam -= napok
            if i.kuldetes_idotartam <= 0:
                i.helyzet = "telephelyen"
                i.kuldetes_idotartam = 0
    with open("kamionok.txt", "w", encoding="utf-8") as file:
                file.write("kamionId;rendszam;teherbiras;fogyasztas;helyzet;kuldetes_idotartam\n")
                for i in kamionok:
                    file.write(f"{i.kamionId};{i.rendszam};{i.teherbiras};{i.fogyasztas};{i.helyzet};{i.kuldetes_idotartam}\n")




# programm

while True:
    opcio = input("\n\n\nMenü: \n\nKamion adatainak lekérése: 1 \nRendszámlekérés: 2 \nMegrendelés: 3 \nKamion fogyasztás lekérése: 4 \nRendelkezésre álló kamion flotta: 5 \nIdő múlás szimulálása: 6 \nKilépés: 0 \n\nFunkció választása: ")
    if opcio == "0":
        print("Kilépés...")
        break
    elif opcio == "1":
        kamionId = int(input("Adja meg a kamion azonosítóját (101-150): "))
        kamion = kamion_adatok_lekeres(kamionId)
        if kamion:
            print(f"Kamion adatai: kamionId: {kamion.kamionId}, Rendszám: {kamion.rendszam}, Teherbírás: {kamion.teherbiras} tonna, Fogyasztás: {kamion.fogyasztas} l/100km, Helyzet: {kamion.helyzet}, Küldetés időtartam: {kamion.kuldetes_idotartam} nap")
        else:
            print("Nincs ilyen kamion.")
    elif opcio == "2":
        kamionId = int(input("Adja meg a kamion azonosítóját (101-150): "))
        rendszam = rendszam_lekeres(kamionId)
        if rendszam:
            print(f"A kamion rendszáma: {rendszam}")
        else:
            print("Nincs ilyen kamion.")
    elif opcio == "3":
        szukseges_kamionok = megrendeles()
        if szukseges_kamionok is not None:
            print("Szükséges kamionok a szállításhoz:")
            for i in szukseges_kamionok:
                print(f"  kamionId: {i.kamionId}, Rendszám: {i.rendszam}, Teherbírás: {i.teherbiras} t")
                i.helyzet = "kuldetesen"
                i .kuldetes_idotartam = random.randint(1, 14)
            
            with open("kamionok.txt", "w", encoding="utf-8") as file:
                file.write("kamionId;rendszam;teherbiras;fogyasztas;helyzet;kuldetes_idotartam\n")
                for i in kamionok:
                    file.write(f"{i.kamionId};{i.rendszam};{i.teherbiras};{i.fogyasztas};{i.helyzet};{i.kuldetes_idotartam}\n")
        else:
            print("Nincs elegendő kapacitás a szállításhoz.")
    elif opcio == "4":
        kamionId = int(input("Adja meg a kamion azonosítóját (101-150): "))
        fogyasztas = fogyasztas_lekeres(kamionId)
        if fogyasztas is not None:
            print(f"A kamion fogyasztása: {fogyasztas} l/100km")
        else:
            print("Nincs ilyen kamion.")
    elif opcio == "5":
        telephelyen_levok, kuldetesen_levok = rendelkezesre_allo_kamion_flotta()
        print(f"Telephelyen lévő kamionok száma: {len(telephelyen_levok)}")
        print(f"Küldetésen lévő kamionok száma: {len(kuldetesen_levok)}")
    elif opcio == "6":
        napok = int(input("Adja meg az eltelt napok számát: "))
        idomulas(napok)
        print(f"{napok} nap eltelt, a kamionok státusza frissítve.")
    else:
        print("Érvénytelen opció, próbálja újra.")
    