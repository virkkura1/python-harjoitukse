import math

luku = int(input("\nAnna kokonaisluku: "))

alkulukuus=True

for jakaja in range(2,math.isqrt(luku)+1,1):
    if luku % jakaja == 0:
        alkulukuus=False

if alkulukuus == True:
    print(luku, "on alkuluku\n")

else:
    print(luku, "ei ole alkuluku\n")
    
