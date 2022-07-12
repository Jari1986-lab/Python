def viiva(merkkijono, leveys):
    print(merkkijono * leveys)

def risulaatikko(korkeus):
    while korkeus > 0:
        viiva("#", 10)
        korkeus -= 1

if __name__ == "__main__":
    risulaatikko(5)
    print()
    risulaatikko(2)
