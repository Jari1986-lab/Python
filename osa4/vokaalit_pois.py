def ilman_vokaaleja(sana):
    if sana == 'x':
        exit()
    else:
        uusi_sana = sana
    vokaalit = ('a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö')
    for x in sana.lower():
        if x in vokaalit:
            uusi_sana = uusi_sana.replace(x,"")
    return uusi_sana

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))
