def lyhin(lista):
    merkkijono = (s for s in lista if isinstance(s, str))
    pituus = min(merkkijono, key=len) if merkkijono else None
    return (pituus)

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = lyhin(lista)
    print(tulos)

    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]
    tulos = lyhin(lista)
    print(tulos)