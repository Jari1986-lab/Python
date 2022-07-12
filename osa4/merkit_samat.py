def samat(merkkijono, sana, sana2):
    try:
        if merkkijono[sana] == merkkijono[sana2]:
            return True

        if merkkijono[sana] != merkkijono[sana2]:
            return False
    
    except:
        return False
if __name__ == "__main__":
    print(samat("koodari", 1, 2)) 
    print(samat("koodari", 0, 4))
    print(samat("koodari", 0, 10))