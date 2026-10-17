#Oikea vastaus
#1 tuuma = 2.54 cm

print("- - -TERVETULOA OHJELMAAN- - ")

luku=float(input("Anna luku tuumina (negatiivinen lopettaa)?"))

#Toista kun luku on suurempi kuin 0
while luku >= 0:

    #tapa päivittää ehtoa
    cm = luku *2.54
    print(f"{luku} tuumaa on {cm} senttiä")
    luku=float(input("Anna luku tuumina(negatiivinen lopettaa)?"))


