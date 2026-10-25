from math import sqrt


while True:

    luku =int(input("\nAnna kokonaisluku/ 0 lopettaa:"))

    if luku == 0:
            break
    elif luku <  0:
        print("Virheelinen luku")

    else:
        print(sqrt(luku))

    
print("Ohjelma lopetettu")