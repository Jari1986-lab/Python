def small_letter(test):
  test2 = []
  for word in test:
    word2 = word
    if word2.islower():
      test2.append(word)
  return test2


test = ["My", "you", "why", "THANKS", "little", "Home", "ABC", "BIG"]
new_list = small_letter(test)
print(new_list)
