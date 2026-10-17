#OIkea vastaus
luku=input ("Anna luku, tyhjä lopettaa:")
pieni=luku
suuri=luku

while luku !="":
    #Muutetaan tekstimuotinen numeto numeroksi
    numero=int(luku)

    #Vertaillaan
    if pieni == luku or numero < pieni:
        pieni = numero
    if suuri == luku or numero < suuri:
        suuri = numero

    luku=input("Anna luku, tyhjä lopettaa:")

print("Pienin luku on", pieni)
print("Suurin luku on", suuri)

