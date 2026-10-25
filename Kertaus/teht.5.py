sanat=[]

sana=input("\nAnna sana lisättäväksi tarinaan: ")

while True:
    sanat.append(sana)
    sana=input("\nAnna sana lisättäväksi tarinaan: ")
    
    if sana =="loppu":
        break

    if len(sanat) > 0 and sana == sanat [-1]:
        break
    
tarina = " ".join(sanat)
print(tarina)
