yrityksia = 1
while True:
    pin = input("PIN-koodi: ")
    if pin == "4321":
        break
    print("Väärin")
    yrityksia += 1
 
if yrityksia == 1:  
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {yrityksia} yritystä")

#yritykset = 0

#while True:
 #   tunnus = input("Anna PIN-koodi: ")
  #  yritykset += 1
    
   # if tunnus == "4321":
    #    onnistui = True
     #   break


    #print("Väärin")

#if onnistui and yritykset == 1: 
 #   print ("Oikein, tarvitsit vain yhden yrityksen!")

    
#elif  onnistui:
 #   print(f"Oikein, tarvitsit {yritykset} yritystä")
