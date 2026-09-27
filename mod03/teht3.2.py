#Harjoitus if/elif/else
#If/elif kuuluu aina yhteen. Eli elif ehto vaatii aina If.

Hyttiluokka=input("Mikä on laivan hyttiluokka?")
if Hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif Hyttiluokka=="A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif Hyttiluokka=="B":  
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif Hyttiluokka=="C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")