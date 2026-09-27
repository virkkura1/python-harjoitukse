komento=input ("Anna komento: ")

while komento!="lopeta":
    if komento == "MAYDAY":
        break
    print("Suoritetaan komento:" +komento)
    komento=input ("Anna uusi komento: ")
else:
    print("Tämä on teksti elsen sisältä")

print("Toiminnot lopetettu")