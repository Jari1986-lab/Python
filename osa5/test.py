def count_element(test, elelemnt):
    count = 0
    for i in test:
        if  i == elelemnt:
            count+=1
    return count

m = [1,2,3,3,4,3,6,3,2,1,2]
print(count_element(m, 2))