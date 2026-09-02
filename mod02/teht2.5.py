# Käyttäjän syöte
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

# Muunnetaan kaikki luodeiksi, koska se on pienin yksikkö
# 1 leiviskä = 20 naulaa = 20*32 = 640 luotia
# 1 naula = 32 luotia
luoteja_yhteensa = leiviska * 20 * 32 + naula * 32 + luoti

# Yksi luoti on 13,3 grammaa
grammoja_yhteensa = luoteja_yhteensa * 13.3

# Muunnetaan täysiksi kiloiksi ja jäljelle jääviksi grammoiksi
kilot = int(grammoja_yhteensa // 1000)
grammat = grammoja_yhteensa % 1000

print(f"Massa nykymittojen mukaan: {kilot} kg ja {grammat:.2f} g")