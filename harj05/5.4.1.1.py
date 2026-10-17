kaupungit=[]

kaupunki=input(str("\nAnna kaupungin nimi?"))

while kaupunki <={5}:
    kaupungit.append(kaupunki[:5])
    
    kaupunki=input("\nAnna kaupungin nimi?")
    
for kaupunki in kaupungit[:5]:
    
    
    print(kaupunki)