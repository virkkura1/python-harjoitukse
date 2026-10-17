import random

# Kysytään käyttäjältä, montako arpakuutiota heitetään
lukumaara = int(input("\nMontako arpakuutiota heitetään? "))

summa = 0

# Heitetään jokainen arpakuutio kerran
for i in range(lukumaara):
    silmaluku = random.randint(1, 6)
    print("Noppa", silmaluku)
    summa = summa + silmaluku

print("Silmälukujen summa on", summa)