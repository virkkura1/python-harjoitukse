#Harjoitus biologisen sukupuolen ja hemoglobiiniarvon (g/l)

sukupuoli=input("Mikä on sinun sukupuoli?")


hemoglobiiniarvo=int(input("Mikä on sinun hemoglobiiniarvo (g/l)?"))

if sukupuoli == "nainen" and hemoglobiiniarvo >=117 and hemoglobiiniarvo <=178:
    print("hemoglobiiniarvo on normaali")
if sukupuoli == "nainen" and hemoglobiiniarvo <117:
    print("hemoglobiiniarvo on matala")
if sukupuoli == "nainen" and hemoglobiiniarvo >178:
    print("hemoglobiiniarvo on korkea")

if sukupuoli == "mies" and hemoglobiiniarvo >=134 and hemoglobiiniarvo <=195:
    print("hemoglobiiniarvo on normaali")
if sukupuoli == "mies" and hemoglobiiniarvo <134:
    print("hemoglobiiniarvo on matala")
if sukupuoli == "mies" and hemoglobiiniarvo >195:
    print("hemoglobiiniarvo on korkea")
