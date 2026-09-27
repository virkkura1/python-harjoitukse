#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1–
#1000.
komento = input("Anna komento:")

while komento!="lopeta":
    if komento == "STOP":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = int(input("Tulosta kolmella jaolliset luvut väliltä 1–_1000"))

else: 
    print ("Näkemiin")

print ("Toiminnot lopetettu")

