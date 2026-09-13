pituus=float(input("Paljon kuhan pituus on?"))

if pituus<37:
    print(f"Kuhan pituus on liian lyhyt {pituus-37} cm. Laske se takaisin järveen.")
else:
    print("Kuha on hyvän mittainen. Voit ottaa sen mukaasi.")