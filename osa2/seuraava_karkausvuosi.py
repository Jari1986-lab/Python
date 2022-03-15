vuosi = int(input("Vuosi: "))

a = vuosi

while True:

    vuosi += 1

    if vuosi % 4 == 0 and (vuosi % 100 != 0 and vuosi % 400 != 0):
        break

    elif vuosi % 100 == 0 and vuosi % 400 == 0:
        break

print(f"Vuotta {a} seuraava karkausvuosi on {vuosi}")