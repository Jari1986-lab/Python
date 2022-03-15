from math import sqrt

while True: 
    a = float(input("Syötä luku: "))
    if a <0:
        print("Epäkelpo luku")
    
    if a > 0:
        print(sqrt(a))
    
    if a == 0:
        break

print("Lopetetaan...")