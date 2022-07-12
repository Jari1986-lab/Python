def eka_sana(merkkijono):
    ensimmainen = merkkijono.split()[0]
    return ensimmainen


def toka_sana(merkkijono):
    toinen = merkkijono.split()[1]
    return toinen

def vika_sana(merkkijono):
   
    uusi_merkkijono = ""
     
   
    pituus = len(merkkijono)
     
   
    for i in range(pituus-1, 0, -1):
       
        
        if(merkkijono[i] == " "):
           
      
            return uusi_merkkijono[::-1]
        else:
            uusi_merkkijono = uusi_merkkijono + merkkijono[i]




if __name__ == "__main__":
    sana = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(sana))
    print(toka_sana(sana))
    print(vika_sana(sana))