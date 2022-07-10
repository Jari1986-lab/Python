sana = input("Anna sana: ")

len1 = sana[1]
len2 = sana[-2]

if sana[1] == sana[-2]:
    print(f"Toinen ja toiseksi viimeinen kirjain on {len1}")
else:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")

#sana = input("Anna sana: ")
 
# Tarkistetaan myös, että pituus on vähintään kaksi merkkiä,
# jotta toinen ja toiseksi viimeinen kirjain ovat olemassa
#if len(sana) > 1 and sana[1] == sana[-2]:
#    print("Toinen ja toiseksi viimeinen kirjain on " + sana[1])
#else:
#   print("Toinen ja toiseksi viimeinen kirjain eroavat")