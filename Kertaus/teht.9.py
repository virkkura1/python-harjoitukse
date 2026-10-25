# Luodaan kaksi tyhjää listaa: toiseen tuotteiden nimet, toiseen määrät
tuotteet = []
maarat = []

# Silmukka toistuu, kunnes käyttäjä vastaa "Ei"
while True:
    # Kysytään tuotteen nimi (teksti, joten int() ei tarvita)
    tuote = input("Mitä tuotetta valmistetaan? ")

    # Kysytään määrä ja muutetaan se luvuksi int():llä
    maara = int(input("Kuinka monta valmistetaan? "))

    # Lisätään nimi ja määrä omiin listoihinsa.
    # Ne menevät samaan kohtaan, joten ne pysyvät "parina"
    tuotteet.append(tuote)
    maarat.append(maara)

    vastaus = input("Jatketaanko tuotantoa? ")

 
    if vastaus.lower() == "ei":
        break


print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")

# Käydään listat läpi järjestysnumeron (indeksin) avulla.
# range(len(tuotteet)) antaa luvut 0, 1, 2, ... listan pituuteen asti
for i in range(len(tuotteet)):
    print(tuotteet[i] + ":", maarat[i], "kpl")