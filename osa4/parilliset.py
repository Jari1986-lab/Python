def parilliset(lista):

    uusi_lista = [num for num in lista if num % 2 == 0]
    return uusi_lista

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    uusi_lista = parilliset(lista)
    print("alkuperäinen", lista)
    print("uusi", uusi_lista)
