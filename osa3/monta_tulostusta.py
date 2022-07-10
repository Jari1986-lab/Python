def apu(merkkijono):
    print(merkkijono)

def tulosta_monesti(merkkijono, kertaa):
    while kertaa > 0:
        apu(merkkijono)
        kertaa -= 1

if __name__ == "__main__":
    tulosta_monesti("Hei", 5)
    tulosta_monesti("Alussa olivat suo, kuokka ja Python", 3)

#def tulosta_monesti(merkkijono, kertaa):
 #   while kertaa > 0:
  #      print(merkkijono)
   #     kertaa -= 1
    
#if __name__ == "__main__":
 #   tulosta_monesti("python", 5)