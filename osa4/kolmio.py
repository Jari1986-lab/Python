def viiva(merkkijono, leveys):
    print(merkkijono * leveys)

def kolmio(koko):
    rivit = 1
    while rivit <= koko:
        viiva ("#", rivit)
        rivit +=1


if __name__ == "__main__":
    kolmio(6)
    print()
    kolmio(3)