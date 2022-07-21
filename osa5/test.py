def count_element(test, elements):
    count = 0
    for i in test:
        count += 1
    return count

m = [1,2,3,3,4,3,6]
print(count_element(m, 3))