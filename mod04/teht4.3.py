
#  Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän
# merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja
# suurimman. Huomioi, että sinun tulee ”pitää kirjaa” siitä, mikä on pienin ja suurin luku.



print("- - - TERVETULOA OHJELMAAN- - -")

pienin = 0
suurin = 0

while True:

    luku =input("Anna luku / xxx lopettaa:")
    
    
    if luku == "xxx":
        break

    luku = (float (luku))

    if pienin == 0 or luku < pienin:
        pienin = luku
    if suurin == 0 or luku > suurin:
        suurin = luku

if pienin == 0:
    print("Et antanut yhtään lukua.")
else:
    print(f"Suurin luku on {suurin}, pienin luku on {pienin}")

print("Ohjelma lopetettu")
