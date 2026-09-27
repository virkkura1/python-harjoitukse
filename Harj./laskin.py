print("- - - - - Tervetuloa laskinohjelmaan- - - - -")

# Yksinkertainen toistorakenne
while True:

    print("Valitse mitä laskintoimintoa haluat käyttää:")
    print("A: Yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku, Q: Lopeta ohjelma")
    valinta= input("Anna valintasi: ").upper()

#Tarkistetaan ehtoa
    if valinta=="Q":
        print("Poistutaan....")
        break

    # Alustetaan muuttujat?
    a = float(input("Anna ensimmmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    
    #Tarkistetaan ehtoa
    if valinta == "A":
        print(f"Lukujen {a} ja {b} summa on {a+b}.")
        
    elif valinta == "B":
        print(f"Lukujen {a} ja {b} erotus on {a-b}.")

    elif valinta == "C":
        print(f"Lukujen {a} ja{b} tulo on {a*b}.")

    elif valinta == "D":
        print(f"Lukujen {a} ja{b} osamäärä on {a/b}.")
        
    else:
        print("Virheellinen valinta")

print("Ohjelma päättynyt.")

# Keksi parempi kohta ilmoittaa virheellisestä valinnasta
# Kommentoi koodi - mitä se tekee missäkin kohdassa?         