lista = []
luku = int(input("Kuinka monta lukua: "))
for laskuri in range (luku):
    luku2 = input (f"Anna luku {laskuri+1}: ")
    lista.append(luku2)
print("[{}]".format(', '.join(lista)))