pisteet = int(input("Kuinka paljon pisteitä? "))
if pisteet < 100:
    pisteet *= 1.1
    print("Sait 10 % bonusta")

elif pisteet >= 100: 
    pisteet *= 1.15
    # 95> 100
    print("Sait 15 % bonusta")

print("Pisteitä on nyt", pisteet)

#print("Kerro huominen sääennuste:")
#lampo = int(input("Lämpötila: "))
#sade = (input("Sataako (kyllä/ei): "))

#print("Pue housut ja t-paita")

#if lampo <= 20:
    # 11 < 20
#    print("Ota myös pitkähihainen paita")

#if lampo <= 10:
 #   print("Pue päälle takki")

#if lampo <=5:
 #   print("Suosittelen lämmintä takkia")
  #  print("Kannattaa ottaa myös hanskat")
    
#if sade == "kyllä":
 #   print("Muista sateenvarjo!")

