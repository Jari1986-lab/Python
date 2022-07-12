def lue_kayttajalta(maara: int):
    print(f"Syötä {maara} lukua:")
    luvut = []

    for i in range(maara):
        luku = int(input("Anna luku: "))
        luvut.append(luku)

    return luvut

def tulosta(luvut: list):
    print("Luvut ovat: ")
    for luku in luvut:
        print(luku)

def analysoi(luvut: list):
    keskiarvo = sum(luvut) / len(luvut)
    return f"Lukuja yhteensä {len(luvut)}, keskiarvo {keskiarvo}, pienin {min(luvut)} ja suurin {max(luvut)}"

# funktioita käyttävä "pääohjelma"
syotteet = lue_kayttajalta(5)
tulosta(syotteet)
analyysin_tulos = analysoi(syotteet)
print(analyysin_tulos)