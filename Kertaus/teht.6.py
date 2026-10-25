arvot=[]

arvo=int(input("\nAnna arvo: "))

while True:
    arvot.append(arvo)
    arvo=int(input("\nAnna arvo: "))

    if arvo == 0:
        break

    

    
print("Lisäysjärjestyksessä",arvot)
print("Pienimmästä suurimaan:",sorted(arvot))