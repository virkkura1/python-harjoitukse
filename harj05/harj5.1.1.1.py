import random
kuutiot=input("Anna arpakiitoiden lukumaaärä?")

while kuutiot == "":

#  numeroa väliltä 1, 2, 3, 4, 5 tai 6
kuutiot =random.randint(1, 6) 

for luku in kuutiot
    print(f"Kuutoiden summa on: {luku} ")