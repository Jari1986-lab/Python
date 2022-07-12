def muotoile(lista):
        lista2= [f"{num:.2f}" for num in lista]
        lista2 = [str(muotoile) for muotoile in lista2]

        return lista2

if __name__ == "__main__":
        lista = [1.234, 0.3333, 0.11111, 3.446]
        lista2 = muotoile(lista)
        print(lista2)
    