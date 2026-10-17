# Oikea vastaus
#  arvo numero väliltä 1_10 ja kysy
# Ohjeessa: tietokone ei saa vaihtaa lukuaan arvontojen välissä-> ei saa olla while loopin sisällä

import random

oikea=random.randint(1, 10)

arvaus=int(input("Anna luku välillä 1-10:"))

while oikea != arvaus:
    if arvaus > oikea:
        print("Liian suuri arvaus")

    else:
        print("Liian pieni arvaus")
    
    arvaus =int(input("Anna luku välillä 1-10:"))
        
print("Oikein")
print("Luku ", oikea, "on oikein")
      