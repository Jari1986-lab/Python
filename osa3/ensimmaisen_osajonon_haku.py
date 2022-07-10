sana = input("Sana：")
merkki = input("merkki：")
index = sana.find(merkki)
if sana.find(merkki) == -1 or len(sana[index:index+3]) < 3:
    print('')
else:
    print(sana[index:index+3])

#sana = input("Sana: ")
#merkki = input("Merkki: ")
 
#kohta = sana.find(merkki)
#if kohta!=-1 and len(sana)>=kohta+3:
 #   print(sana[kohta:kohta+3])