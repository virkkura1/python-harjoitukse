import math

def keskiarvo(luku1, luku2, luku3):
    k=(luku1+luku2+luku3)/3 
    return k

luku1=int(input("Anna ensimmäinen luku?"))
luku2=int(input("Anna toinen luku?"))
luku3=int(input("Anna kolmas luku?"))
tulos=keskiarvo(luku1, luku2, luku3)
print(f"Lukujen {luku1} ja {luku2} ja {luku3} keskiarvo on {tulos}.")