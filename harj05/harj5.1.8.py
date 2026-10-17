# Tee tämä harjoitus itse loppun , vastaus

ostokset=["maito", "liha", "juusto", "keksi"]
tieto=input("MItä on ostoslistalla? ")
if "tieto" in ostokset:
    print("Tuote on listassa")

    while num != 0:
    numerot.append(num)
    num =int(input("Anna numero listaan: "))

summa = 0

print(numerot)

print("Tulostetaan nimet")

for numero in numerot:
    summa += numero
    print("Ostoslistalla: ", summa)

print("Ohjelma loppui.")
else:
    print("Tuote ei ole listassa")
