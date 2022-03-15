tarina = ""
edellinen = ""
while True:
    sana = input("Anna sana: ")
    if sana == "loppu" or sana == edellinen:
        break
    tarina += sana + " "
    edellinen = sana
 
print(tarina)

#vali = " " 
#lisaa = "" 
#edellinen =" "
#quit = False

#while not quit:
 #   sana = (input("Anna sana: "))
  #  quit = sana == edellinen or sana == 'loppu'
   # if not quit:
    # lisaa += sana + vali
     #edellinen = sana
    
#print(lisaa)