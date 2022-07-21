import re
lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
regex = re.compile("[a-z]+")
print(list(filter(regex.search, lista)))