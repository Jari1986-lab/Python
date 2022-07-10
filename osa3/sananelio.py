def nelio(word,size):
    i = 0
    for line in range(size):
        for char in range(size):
            print(word[i % len(word)], end="")
            i += 1
        print()

if __name__ == "__main__":
    nelio("ab",3)
    print()
    nelio("aybabtu",5) 


#def nelio(merkit, koko):
 #   i = 0
  #  rivi = ""
   # while i < koko * koko:
    #    if i > 0 and i % koko == 0:
     #       print(rivi)
      #      rivi = ""
       # rivi += merkit[i % len(merkit)]
        #i += 1
    #print(rivi)