def anagrammi(s1, s2):
    try: 
        if (sorted(s1)== sorted(s2)):
            return True
        if (sorted(s1) != sorted(s2)):
            return False
    except:
            return False
    
if __name__ == "__main__":
              
    print(anagrammi("talo", "tola")) 
    print(anagrammi("talo", "lato")) 
    print(anagrammi("talo", "olat")) 
    print(anagrammi("tammi", "mitta")) 
    print(anagrammi("python", "java")) 