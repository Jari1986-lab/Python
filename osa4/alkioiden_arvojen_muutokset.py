lista = [1,2,3,4,5]

while True:
    index = int(input("Anna indeksi: "))
    if  index == -1:
        break
    arvo = int(input("Anna arvo: "))
    lista.pop(index)
    lista.insert(index, arvo)
    print (lista)
