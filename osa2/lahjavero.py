suuruus = int(input("Lahjan suuruus: "))
 
if suuruus < 5000:
    vero = 0
elif suuruus <= 25000:
    vero = 100 + (suuruus - 5000) * 0.08
elif suuruus <= 55000:
    vero = 1700 + (suuruus - 25000) * 0.10
elif suuruus <= 200000:
    vero = 4700 + (suuruus - 55000) * 0.12
elif suuruus <= 1000000:
    vero = 22100 + (suuruus - 200000) * 0.15
else:
    vero = 142100 + (suuruus - 1000000) * 0.17
 
if vero == 0:
    print("Ei veroa!")
else:
    print(f"Vero: {vero} euroa")
    
#lahja = float(input("Lahjan suuruun? "))

#if lahja < 5000:
 #   print("ei veroa!")

#elif lahja >= 5000 and lahja <= 25000:
 #   vero = 100 + (lahja-5000)* 0.08
  #  print(f"Vero: {vero} euroa")

#elif lahja > 2500 and lahja <= 55000:
 #   vero = 1700 + (lahja-25000)* 0.10
  #  print(f"Vero: {vero} euroa")

#if lahja > 55000 and lahja <= 200000:
 #   vero = 4700 + (lahja - 55000)* 0.12
  #  print(f"Vero: {vero} euroa")

#if lahja > 200000 and lahja <= 1000000:
 #   vero = 22100 + (lahja - 200000)* 0.15
  #  print(f"Vero: {vero} euroa")
    
#if lahja > 1000000:
 #   vero = 142100 + (lahja - 1000000)* 0.17
  #  print(f"Vero: {vero} euroa")