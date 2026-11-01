import random

def noppa():
    return random.randint(1,6)


#PÄÄOHJELMA#
print("Heitän noppaa:")
silmäluku=0

#Tarvitaan silmukka toistoja varten
while silmäluku != 6:
    silmäluku = noppa()
    print(f"Silmäluku on {silmäluku}.")