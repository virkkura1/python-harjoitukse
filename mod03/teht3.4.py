#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
#Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat
#karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

karkausvuosi=int(input("Mikä vuosi nyt on?"))
if karkausvuosi % 4 == 0 and (karkausvuosi %100 != 0 or karkausvuosi %400==0):
    print(f"{karkausvuosi} on karkausvuosi")
else:
    print(f"{karkausvuosi} ei ole karkausvuosi")