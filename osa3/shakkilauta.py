def shakkilauta(n):
    finalSentence1 = ""
    finalSentence2 = ""
    for i in range(n): #we add 0 and 1 as much as we have n
        if i%2 == 0: #
            finalSentence1 += "1"
            finalSentence2 += "0"
        else:
            finalSentence1 += "0"
            finalSentence2 += "1"


    for i in range(n): #we print as much as we have n
        if i%2 == 0:
            print(finalSentence1)
        else:
            print(finalSentence2)


if __name__ == "__main__":
    shakkilauta(3)
    print()
    shakkilauta(6)


#def shakkilauta(koko):
 #   i = 0
  #  while i < koko:
   #     if i % 2 == 0:
    #        rivi = "10"*koko
     #   else:
      #      rivi = "01"*koko
        # poistetaan rivin lopusta ylimääräiset merkit
      #  print(rivi[0:koko])
       # i += 1