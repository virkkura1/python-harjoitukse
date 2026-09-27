print("- - - TERVETULOA OHJELMAAN- - -")



tunnus = "Matti"
salasana = "Mikko"
    

while True:

    tunnus =input("Anna tunnus:")
    salasana =input ("Anna salasana?")
    

    if tunnus == "Matti" and salasana == "Mikko":
        print ("Tervetuloa!")
        break

    if tunnus != "Matti"  or salasana != "Mikko":
        print("Pääsy evätty")
    
    break



print("Ohjelma lopetettu")

        
    
