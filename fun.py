def positive(test):
    total = 0
    for element in test:
        if element >= 0:
            total += element
    return total

test2 = [1, -2, 3, -4, 5]
total= positive(test2)
print(total)
