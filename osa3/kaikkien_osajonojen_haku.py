sana = input("Sana: ")
merkki = input ("Merkki: ")
i = sana.find(merkki)
l = len(sana)
while i != -1:
    if l-i >= 3:
        print(sana[i:i+3])
    i = sana.find(merkki, i+1)

#sana = input("Sana: ")
#merkki = input("Merkki: ")
 
#kohta = 0
 
#while kohta + 3 <= len(sana):
 #   if sana[kohta] == merkki:
  #      print(sana[kohta:kohta+3])
   # kohta += 1