def pisimmat(lista):
    merkkijono = [s for s in lista if isinstance(s, str)]
    pisimmat = max([len(x) for x in merkkijono])
    yhta_pitkat=[x for x in merkkijono if len(x)==pisimmat]
    return yhta_pitkat

if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]

    tulos = pisimmat(lista)
    print(tulos)