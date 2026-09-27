print("- - - TERVETULOA OHJELMAAN- - -")

summa=0

while True:

    luku =input("Anna luku /  - lopettaa:")
    
    
    if luku == "xxx":
        break

        print("Ohjelma lopetettu")

    summa = summa + float(luku)
 
print(f"Lukujen summa on: {summa}")
print("Ohjelma lopetettu")