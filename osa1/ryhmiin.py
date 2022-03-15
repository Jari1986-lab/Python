opiskelija = int(input("Montako opiskelijaa? "))
ryhmä = int(input("Mikä on ryhmän koko? ")) 
tulos   = opiskelija // ryhmä
if opiskelija%ryhmä !=0:
    tulos  += 1
print(f"Ryhmien määrä: ", (tulos))
