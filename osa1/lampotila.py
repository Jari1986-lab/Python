fahrenheit = int(input("Anna lämpötila (F): "))
tulos = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} fahrenheit-astetta on {tulos} celsius-astetta") 

if tulos < 0:
    print("Paleltaa!")