laskin = 0
sana2 = []
while True:
    sana = input("Sana: ")
    if sana in sana2:
        break
    else:
        sana2.append(sana)
    laskin+= 1
print(f"Annoit {laskin} eri sanaa")
