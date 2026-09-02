import random
# 3 numeroa väliltä 1, 2, 3, 4, 5 tai 9 
luku1 =random.randint(1, 9)
luku2 =random.randint(1, 9)
luku3 =random.randint(1, 9)
luku4 =random.randint(1, 6)
luku5 =random.randint(1, 6)
luku6 =random.randint(1, 6)
luku7 =random.randint(1, 6)
koodi1=f"{luku1}{luku2}{luku3}"
koodi2=f"{luku4}{luku5}{luku6}{luku7}"
print(f"Arvottu koodi on: {koodi1} ja {koodi2}")