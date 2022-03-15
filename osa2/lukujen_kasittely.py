print("Syötä kokonaislukuja, 0 lopettaa:")
lukuja = 0
summa = 0
positiivisia = 0
 
while True:
    luku = int(input("luku: "))
    if luku == 0:
        break
    lukuja += 1
    summa += luku
    if luku>0:
        positiivisia += 1
 
print("Lukuja yhteensä", lukuja)
print("Lukujen summa", summa)
print("Lukujen keskiarvo", summa/lukuja)
print("Positiivisia", positiivisia)
print("Negatiivisia", lukuja-positiivisia)

#print("Syötä kokonaislukuja, 0 lopettaa: ")
#summa = 0
#maara = 0
#maara2 = 0
#maara3 = 0
#quit = False
#while not quit:
 #   luku = int(input("Luku: "))
  #  quit = luku == 0
   # if luku > 0:
    #    maara2 += 1
    #if luku < 0:
     #   maara3 += 1
    #if not quit:
     #maara += 1
     #summa = summa + luku
     #keskiarvo = summa / maara
    
#print("...lukujen kysely")
#print(f"Lukuja yhteensä {maara}")
#print(f"Lukujen summa {summa}")
#print (f"Lukujen keskiarvo {keskiarvo}")
#print(f"Positiivisia {maara2}")
#print(f"Negatiivisia {maara3}")