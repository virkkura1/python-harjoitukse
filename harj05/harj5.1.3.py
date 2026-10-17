#Tarkistettu

nimet = []

nimi= input("Anna joku nimi: ")

while nimi !=" ":
    nimet.append(nimi)
    nimi = input("Anna joku nimi: ")

print(nimet)

print("Tulostetaan nimet")

for n in nimet:
    print(f"Terve, {n}!")

print("Ohjelma loppui.")

    