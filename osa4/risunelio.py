def viiva(merkkijono, leveys):
    print(merkkijono * leveys)

def risunelio(koko):
    rivit = koko
    while rivit > 0:
        viiva ("#", koko)
        rivit -=1


if __name__ == "__main__":
    risunelio(5)
    print()
    risunelio(3)