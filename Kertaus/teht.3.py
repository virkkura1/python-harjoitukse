while True:
    print("Tuote valmistettu!")
    vastaus = input("Jatketaanko tuotantoa? ")

    if vastaus.lower() == "ei":
        break

print("Tuotanto lopetettu!")