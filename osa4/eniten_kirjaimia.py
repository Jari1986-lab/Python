from collections import Counter

def eniten_kirjainta(sana):

    res = Counter(sana)
    res = max(res, key = res.get)
    return res

if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))