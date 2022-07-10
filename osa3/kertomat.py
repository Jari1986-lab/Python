kertoma = 1
luku= 1
 
while True:
    numero = int(input("Anna luku: "))
    if numero < 1:
        print("Kiitos ja moi!")
        break
    elif luku <= numero:
        for luku in range (1, numero+1):
            kertoma = kertoma * luku
        print (f"Luvun {numero} kertoma on {kertoma}")
    else:
        continue
    
    kertoma = 1
    luku = 1


#while True:
 #   luku = int(input("Anna luku: "))
  #  if luku <= 0:
   #     break
 
    #kertoma = 1
    #uusi = 1
    #while uusi <= luku:
     #   kertoma *= uusi
      #  uusi += 1
 
    #print(f"Luvun {luku} kertoma on {kertoma}")
 
#print("Kiitos ja moi!")