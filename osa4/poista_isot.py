def poista_isot(lista):
        lista2 = []
        for sana in lista:
                for kirjain in sana:
                        if kirjain.islower():
                                lista2.append(sana)
                                break
        return lista2

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)
