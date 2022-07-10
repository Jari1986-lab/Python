rajaus = input("Sana: ")
kehys = 30
print('*'*kehys)
print(rajaus.center(kehys-2, ' ').center(kehys, '*'))
print('*'*kehys)

#sana = input("Sana: ")
 
#print("*" * 30)
#alkuvalit = (28 - len(sana)) // 2
#loppuvalit = alkuvalit
 
# Jos sanan pituus on pariton, lisätään loppuväliin 1
# jotta saadaan täydet 30 merkkiä
#if len(sana) % 2 != 0:
 #   loppuvalit += 1
 
#print("*" + alkuvalit * " " + sana + loppuvalit * " " + "*")
#print("*" * 30)
