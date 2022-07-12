def kaikki_vaarinpain(lista):
        lista2 = [i[::-1] for i in lista[::-1]]
        return lista2

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)