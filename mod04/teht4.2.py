#Ohjelma tuumat senteiksi VALMIS.


print("- - -TERVETULOA OHJELMAAN- - ")

luku=float(input("Anna luku tuumina?"))

#Toista kun luku on suurempi kuin 0
while luku>0:

    #tapa päivittää ehtoa
    print(f"Luku on {luku*2.54:.2f} senttiä")
    luku=float(input("Anna luku tuumina?"))

    if luku < 0:
        break

print("Ohjelma loppuu")


