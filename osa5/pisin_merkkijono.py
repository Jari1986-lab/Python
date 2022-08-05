def pisin(lista:list):
    pisin2 = -1
    for vertaa in lista:
        if len(vertaa) > pisin2:
            pisin2 = len(vertaa)
            vastaus = vertaa
    return vastaus

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))
