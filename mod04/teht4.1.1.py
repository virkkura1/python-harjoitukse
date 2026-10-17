#OIkea vastaus
luku = 1
while luku <= 1000:
    #Tarkistetaan onko luku jaollinen kolmella
    if luku % 3 == 0:
        print(luku)
    #miten saadaan, että ei mene ikuiseen looppiin
    luku += 1