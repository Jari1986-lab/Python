pisteet = int(input("Anna pisteet [0-100]: "))
 
if pisteet < 0 or pisteet > 100:
    arvosana = "mahdotonta!"
elif pisteet < 50:
    arvosana = "hylätty"
elif pisteet < 60:
    arvosana = "1"
elif pisteet < 70:
    arvosana = "2"
elif pisteet < 80:
    arvosana = "3"
elif pisteet < 90:
    arvosana = "4"
else:
    arvosana = "5"
 
print(f"Arvosana: {arvosana}")

#arvosana = int(input("Anna pisteet[0-100]: "))
   
#if arvosana < 0:
 #  print("Arvosana: mahdotonta!")

#if arvosana >=0 and arvosana <=49:
 #  print("hylätty")
   
#if arvosana >= 50 and arvosana <= 59:
 #  print("Arvosana: 1")
   
#if arvosana >= 60 and arvosana <=69:
 #  print("Arvosana: 2")
   
#if arvosana >= 70 and arvosana <= 79:
 #  print("Arvosana: 3")
   
#if arvosana >= 80 and arvosana <= 89:
 #  print("Arvosana: 4")

#if arvosana >= 90 and arvosana <= 100:
 #  print("Arvosana: 5")
   
#if arvosana > 100:
 #  print("Arvosana: mahdotonta!")