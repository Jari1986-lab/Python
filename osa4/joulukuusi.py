def joulukuusi(koko):
    print("joulukuusi!")
    print("\n".join([f"{'*'*(2* n + 1):^{2*koko-1}}" for n in (*range(koko), 0)]))
if __name__ == "__main__":
    joulukuusi(3)
 