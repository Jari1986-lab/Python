def viiva(merkkijono, leveys):
    print(merkkijono * leveys)

def nelio(koko, merkkijono):
    rivit = koko
    while rivit > 0:
        viiva (merkkijono, koko)
        rivit -=1


if __name__ == "__main__":
    nelio(5, "*")
    print()
    nelio(3, "o")