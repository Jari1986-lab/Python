from math import sqrt

a = float(input("Anna a: "))
b = float(input("Anna b: "))
c = float(input("Anna c: "))
d = b *b -4 * a * c

x1 = (-b + sqrt(d)) / (2* a)
x2 = (-b - sqrt(d)) / (2* a)
print(x1, x2)