def eka_sana(merkkijono):
    ensimmainen = merkkijono.split()[0]
    return ensimmainen


def toka_sana(merkkijono):
    toinen = merkkijono.split()[1]
    return toinen

def vika_sana(merkkijono):
    viimeinen = merkkijono.split()[-1]
    return viimeinen


sana = "olipa kerran kauan sitten ohjelmoija"

print(eka_sana(sana))
print(toka_sana(sana))
print(vika_sana(sana))