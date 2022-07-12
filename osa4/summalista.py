def summa (a, b):
    summa = [x + y for (x, y) in zip(a, b)] 
    return summa

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b))