lista = []
luku2 = 0
print("Lista on nyt []")
while True:
    luku = (input("(l)isää, (p)oista vai e(x)it: "))
    if luku == "l":
        luku2 +=1
        lista.append(luku2)
    elif luku == "p":
        luku2 -=1
        lista.pop(luku2)
    elif luku == "x":
        break
    print(f"Lista on nyt {lista}")
print("Moi!")