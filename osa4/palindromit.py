def palindromi(sana: str):
    if sana != sana[::-1]:
        return False    
    elif sana == sana[::1]:
        return True
 
while True:
    s = input("Anna Palindromi: ")
    s2 = palindromi(s)

    if s2:
        print(f"{s} on palindromi!")
    if s2:
        break
    print("ei ollut palindromi")
                