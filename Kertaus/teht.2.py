# If harjoitus

luku = int(input("\nAnna kokonaisluku: "))

if luku % 3 == 0 and luku % 5 == 0:
        print("Jaollinen molemmilla luvuilla\n")

elif luku % 5 == 0:
    alkulukuus=False
    print("viidellä jaollinen\n")

elif luku % 3 == 0:
    alkulukuus=False
    print("kolmella jaollinen\n")



else:
    print("Ohjelma loppuu\n")