def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat 


#PÄÄOHJELMA

while True:
    maara = float(input("\nAnna gallonamäärä?"))

    if maara  < 0:
        print("Ohjelma loppuu")
        break

    tulos = gallonat_litroiksi(maara)
    print(f"{maara} gallonaa on {tulos:.2f} litraa.")


