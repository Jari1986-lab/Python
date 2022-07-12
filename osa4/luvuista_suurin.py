def luvuista_suurin(a, b, c):
    if a > b:
        return a
    if b > c:
        return b
    else:
        return c
if __name__ == "__main__":
   print(luvuista_suurin(3, 4, 1))
   print(luvuista_suurin(99, -4, 7))
   print(luvuista_suurin(0, 0, 0))