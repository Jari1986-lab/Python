def pisimman_pituus(lista):
    merkkijono = (s for s in lista if isinstance(s, str))
    pituus = max(merkkijono, key=len) if merkkijono else None
    return len(pituus)

if __name__ == "__main__":
    lista = ["eka", "toka", "kolmas", "seitsemäs"]
    tulos = pisimman_pituus(lista)
    print(tulos)