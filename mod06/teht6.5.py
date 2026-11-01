def karsi_parittomat(luvut):
    uusi = []
    for luku in luvut:
        if luku % 2 == 0:
            uusi.append(luku)
    return uusi


# PÄÄOHJELMA

lista = [1, 3, 4, 6, 7, 8, 9]

karsittu = karsi_parittomat(lista)

print("Alkuperäinen lista:", lista)
print("Karsittu lista:", karsittu)