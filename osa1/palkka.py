tuntipalkka = float(input("Tuntipalkka: "))
tunnit = int(input("Työtunnit: "))
viikonpaiva = input("Viikonpäivä: ")
 
if viikonpaiva == "sunnuntai":
    # Sunnuntailta saa tuplapalkan
    tuntipalkka *= 2
 
palkka_yhteensa = tuntipalkka * tunnit
print(f"Palkka {palkka_yhteensa} euroa")