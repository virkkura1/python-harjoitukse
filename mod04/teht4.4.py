import random
#  arvo numero väliltä 1_10 ja kysy

print("- - - TERVETULOA OHJELMAAN- - -")

oikea=random.randint(1, 10)



while True:
    
    arvaus=int(input("Anna luku välillä 1-10:"))

    if oikea > arvaus:
        
        print("Liian pieni arvaus")

            
            
    elif oikea < arvaus:
        arvaus =input("Anna luku välillä 1-10:")
        print("Liian suuri arvaus")
        

    else:

        print("Oikein")
        break
        

print("Toiminnot lopetettu")