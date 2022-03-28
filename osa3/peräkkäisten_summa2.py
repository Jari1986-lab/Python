asti = int(input("Mihin asti: "))
num = asti
i = 1
string = ""
total = 0

while asti >= i and total < asti:
    total += i
    if asti == i or total >= asti:
     string = string + f" {i} ="
    elif asti != i:
     string = string + f" {i} +"  
    i  += 1
    
print (f"Laskettiin{string} {total}")

#asti = int(input("Mihin asti: "))
#luku = 1
#summa = 1
#luvut = "1"
#while summa < asti:
 #   luku += 1
 #  summa += luku
   
   # luvut += f" + {luku}" 
#print(f"Laskettiin {luvut} = {summa}")