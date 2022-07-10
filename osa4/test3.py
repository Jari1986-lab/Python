def uniikit(lista):
  x = []
  for a in lista:
    if a not in x:
      x.append(a)
  return sorted(x)

lista = [3, 2, 2, 1, 3, 3, 1]
print(uniikit(lista))