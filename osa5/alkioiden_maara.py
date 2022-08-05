def laske_alkiot(matriisi: list, alkio: int):
    laske = 0
    for i in matriisi:
        for n in i:
            if  n == alkio:
                laske+=1
    return laske

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))