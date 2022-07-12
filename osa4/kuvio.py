def viiva(merkkijono, leveys):
    print(merkkijono * leveys)

def kuvio(koko, merkkijono, koko2, merkkijono2):
    rivit = 1
    while rivit <= koko:
        viiva (merkkijono, rivit)
        rivit +=1
    rivit = koko2
    while rivit >0:
        viiva(merkkijono2, koko)
        rivit-=1
    


if __name__ == "__main__":
    kuvio(5, "X", 3, "*")
    print()
    kuvio(2, "o", 4, "+")
    print()
    kuvio(3, ".", 0, ",")