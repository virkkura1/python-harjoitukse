import random

def noppa(tahkot):
    return random.randint(1, tahkot)


#PÄÄOHJELMA#
maksimi = int(input("\nAnna maksimisilmäluku?"))
silmaluku=0

#Tarvitaan silmukka toistoja varten
while silmaluku < maksimi:
    silmaluku = noppa(maksimi)
    print(f"Silmäluku on {silmaluku}.")