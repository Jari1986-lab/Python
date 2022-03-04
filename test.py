pisteet = int(input("Kuinka paljon pisteitä? "))

pisteet *= 1.1
if pisteet < 100:
   
    print("Sait 10 % bonusta")



pisteet *= 1.15
if pisteet >= 100:
    
    print("Sait 15 % bonusta")

print("Pisteitä on nyt", pisteet)



 
