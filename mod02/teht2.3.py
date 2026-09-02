#suorakulmion pinta-ala

kanta=float(input("Mikä on suorakulmion kanta? "))
korkeus=float(input("Mikä on suorakulmion korkeus? "))
area=kanta*korkeus
piiri=2*(kanta+korkeus)
print(f"Suorakulmion piiri on {piiri:.2f}")
print(f"Suorakulmion pinta-ala on {area:.2f}")