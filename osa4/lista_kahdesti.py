lista = []

while True:
    luku = int(input("Anna luku: "))
    if luku == 0:
        break
    lista.append(luku)
    print(f"Lista: {lista}")
    print("Järjestettynä: ", end= "")
    print(sorted(lista))
    
print("Moi!")
