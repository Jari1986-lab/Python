import statistics

a1 = input("Anna 1.kirjain: ")
a2 = input("Anna 2.kirjain: ")
a3 = input("Anna3.kirjain: ")
print ("Keskimmäinen kirjain on ", end='')
print(statistics.median( [a1, a2, a3]))
