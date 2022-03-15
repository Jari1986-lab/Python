luku = int(input("Luku 1: "))
luku2 = int(input("Luku 2: "))
komento =(input("Komento: "))


summa = luku + luku2
if komento == "summa":
    print(f"{luku} + {luku2} = {summa}")

tulo = luku * luku2
if komento == "tulo":
    print(f"{luku} * {luku2} = {tulo}")

erotus = luku - luku2
if komento == "erotus":
    print(f"{luku} - {luku2} = {erotus}")