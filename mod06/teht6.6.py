import math

def yksikkohinta(halkaisija_cm, hinta):
    halkaisija_m = halkaisija_cm / 100    
    sade_m = halkaisija_m / 2             
    pinta_ala = math.pi * sade_m ** 2
    return hinta / pinta_ala

#PÄÄOHJELMA#
halkaisija1 = float(input("\nAnna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("\nAnna ensimmäisen pizzan hinta (€): "))
halkaisija2 = float(input("\nAnna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("\nAnna toisen pizzan hinta (€): "))

yh1 = yksikkohinta(halkaisija1, hinta1)
yh2 = yksikkohinta(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta on {yh1:.2f} €/m²")
print(f"Toisen pizzan yksikköhinta on {yh2:.2f} €/m²")

if yh1 < yh2:
    print("Ensimmäinen pizza on parempi vastine rahalle.")
else:
    print("Toinen pizza on parempi vastine rahalle.")