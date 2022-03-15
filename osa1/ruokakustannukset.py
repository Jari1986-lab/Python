unicef = float(input("Montako kertaa viikossa syöt Unicafessa? "))
unicef2 = float(input("Unice-lounaan hinta? "))
ruoka = float(input("Paljonko käytät viikossa ruokaostoksiin? "))
viikko = unicef * unicef2 + ruoka
paiva = viikko / 7
print("Kustannukset keskimäärin: ")
print (f"Päivässä {paiva} euroa")
print (f"Viikossa {viikko} euroa")