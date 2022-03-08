print("Kerro huominen sääennuste:")

sade = (input("Sataako (kyllä/ei): "))

print("Pue housut ja t-paita")

if lampo <= 20:
    # 11 < 20
    print("Ota myös pitkähihainen paita")

if lampo <= 10:
    print("Pue päälle takki")

if lampo <=5:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")
    
if sade == "kyllä":
    print("Muista sateenvarjo!")